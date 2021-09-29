const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const userSchema = new Schema ({
    name: String,
    username: String,
    password: String,
    //Create Schema for portfolio
    //Create Schema for watchlist
    //Create Schema for wallet


}, {
    timestamps: true,
});

const User = mongoose.model('Cryptocurrency', userSchema);
module.export = User;