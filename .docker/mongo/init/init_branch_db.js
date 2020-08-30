db.createUser(
    {
        user : "branch_user",
        pwd  : "branch_password",
        roles : [
            {
                role : "readWrite",
                db   : "branch_db"
            }
        ]
    }
)