const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const stockSchema = new Schema ({
    ticker: String,
    name: String,
    price: Number,
    company_name: String,
    price_change: Number,
    market_high: Number,
    market_low: Number,
    number_invested: Number,
    total_invested: Number


}, {
    timestamps: true,
});

const Stock = mongoose.model('Cryptocurrency', stockSchema);
module.export = Stock;