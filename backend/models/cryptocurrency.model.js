const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const cryptoSchema = new Schema ({
    name: String,
    price: Number,
    price_change: Number,
    number_invested: Number,
    total_invested: Number


}, {
    timestamps: true,
});

const Crypto = mongoose.model('Cryptocurrency', cryptoSchema);
module.export = Crypto;