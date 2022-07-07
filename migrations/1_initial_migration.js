const Migrations = artifacts.require("Migrations");
const Gesetzblatt = artifacts.require("Gesetzblatt");
const Urne = artifacts.require("Urne");
const WahlOrga = artifacts.require("WahlOrga");
const WahlToken = artifacts.require("WahlToken");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(Gesetzblatt);
  //deployer.deploy(Urne);
  deployer.deploy(WahlOrga);
  deployer.deploy(WahlToken);
};
