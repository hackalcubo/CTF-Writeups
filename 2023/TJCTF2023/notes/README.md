# notes

## Flag

tjctf{du1y_n0t3d_b57687e5}

## Solution

The web application shows the flag in the `/` endpoint if a valid session id from an user profile which has been deleted from the database is used:

```JavaScript
app.get('/', (req, res) => {
    if (!req.session.user_id) {
        return res.redirect('/login?e=login%20to%20make%20notes');
    }

    pool.query(`SELECT * FROM notes WHERE user_id = '${req.session.user_id}';`, (err, results) => {
        pool.query(`SELECT * FROM users WHERE id = '${req.session.user_id}';`, (err, users) => {
            res.render('index', { notes: results, user: users[0] || { username: flag } });
        });
    });
});
```

The web application also has a `/user/delete` endpoint which is vulnerable to SQL injection:

```JavaScript
app.post('/user/delete', (req, res) => {
    const id = req.session.user_id;

    pool.query(`DELETE FROM users WHERE id = '${id}' AND password = '${req.body.password}';`, (err, results) => {

        pool.query(`SELECT * FROM users WHERE id = '${id}' AND password != '${req.body.password}';`, (err, results) => {

            if (err)
                return res.redirect('/?e=an%20error%20occurred');

            if (results.length !== 0)
                return res.redirect('/?e=incorrect%20password');

            sessions[id].forEach(session => {
                session.destroy();
            });

            pool.query(`DELETE FROM notes WHERE user_id = '${id}';`, (err, results) => {
                if (err) {
                    res.json({ success: false, message: err });
                } else {
                    res.redirect('/');
                }
            });
        });
    });
});
```

We have to make sure that the `DELETE` query deletes the user profile from our current session and `results.length !== 0` so that `session.destroy();` does not get executed, then we still have a valid session id even if the user profile has been deleted from the database.

So, we create many user profiles and use the payload `YOUR_PASSWORD' or FLOOR(RAND()*2)=1 ; -- -` as the password. The first query deletes the user profile from the database since `password = 'YOUR_PASSWORD` is "true" and the second query
can return some rows since `FLOOR(RAND()*2)=1` can be "true" on some rows. Since we created many users the attack will probably succeed. Then, we navigate to `/` to check whether the attack succeeded and to obtain the flag.
