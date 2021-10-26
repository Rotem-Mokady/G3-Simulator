CREATE TABLE user (
  user_id TEXT PRIMARY KEY,
  user_name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL
);