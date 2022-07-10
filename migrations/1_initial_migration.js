const LiquidDemocracy = artifacts.require("LiquidDemocracy");

module.exports = function (deployer) {
  deployer.deploy(LiquidDemocracy);
};
