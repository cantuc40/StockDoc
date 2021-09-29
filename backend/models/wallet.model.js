const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const walletSchema = new Schema ({
    funds: Number

    
}, {
    timestamps: true,
});

const Wallet = mongoose.model('Cryptocurrency', walletSchema);
module.export = Wallet;