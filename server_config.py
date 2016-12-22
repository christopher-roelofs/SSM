import json
import os.path

configFile = "starbound_server.config"
config = ''



class ServerConfig:
    def __init__(self):
        self.allowAdminCommands = "false"
        self.allowAdminCommandsFromAnyone = "false"
        self.allowAnonymousConnections = "false"
        self.allowAssetsMismatch = "true"
        self.anonymousConnectionsAreAdmin = "false"
        self.bannedIPs = []
        self.bannedUuids = []
        self.checkAssetsDigest = "false"
        self.clearPlayerFiles = "false"
        self.clearUniverseFiles = "false"
        self.clientIPJoinable = "false"
        self.clientP2PJoinable = "true"
        self.configuration = {"basic": "1","server":"4"}
        self.crafting = {"filterHaveMaterials": "false"}
        self.gameServerBind = "::"
        self.gameServerPort = "21025"
        self.interactiveHighlight = "true"
        self.inventory = {"pickupToActionBar": "true"}
        self.maxPlayers = "8"
        self.maxTeamSize = "4"
        self.playerBackupFileCount = "3"
        self.queryServerBind = "::"
        self.queryServerPort = "21025"
        self.rconServerBind = "::"
        self.rconServerPassword = ""
        self.rconServerPort = "21026"
        self.rconServerTimeout = "1000"
        self.runQueryServer = "false"
        self.runRconServer = "false"
        self.safeScripts = "true"
        self.scriptInstructionLimit = "10000000"
        self.scriptInstructionMeasureInterval = "10000"
        self.scriptProfilingEnabled = "false"
        self.scriptRecursionLimit = "100"
        self.serverFidelity = "automatic"
        self.serverName = "A Starbound Server"
        self.serverOverrideAssetsDigest = "null"
        self.serverUsers = []
        self.tutorialMessages = "true"






def readConfig():
    thisConfig = ServerConfig()
    try:
        with open(configFile) as data_file:
            data = json.load(data_file)
            thisConfig.allowAdminCommands = data['allowAdminCommands']
            thisConfig.allowAdminCommandsFromAnyone = data['allowAdminCommandsFromAnyone']
            thisConfig.allowAnonymousConnections = data['allowAnonymousConnections']
            thisConfig.allowAssetsMismatch = data['anonymousConnectionsAreAdmin']
            thisConfig.checkAssetsDigest = data['checkAssetsDigest']
            thisConfig.clearPlayerFiles = data['clearPlayerFiles']
            thisConfig.clearUniverseFiles = data['clearUniverseFiles']
            thisConfig.clientIPJoinable = data['clientIPJoinable']
            thisConfig.clientP2PJoinable = data['clientP2PJoinable']
            thisConfig.gameServerBind = data['gameServerBind']
            thisConfig.gameServerPort = data['gameServerPort']
            thisConfig.interactiveHighlight = data['interactiveHighlight']
            thisConfig.maxPlayers = data['maxPlayers']
            thisConfig.maxTeamSize = data['maxTeamSize']
            thisConfig.playerBackupFileCount = data['playerBackupFileCount']
            thisConfig.queryServerBind = data['queryServerBind']
            thisConfig.queryServerPort = data['queryServerPort']
            thisConfig.rconServerBind = data['rconServerBind']
            thisConfig.rconServerPassword = data['rconServerPassword']
            thisConfig.rconServerPort = data['rconServerPort']
            thisConfig.rconServerTimeout = data['rconServerTimeout']
            thisConfig.runQueryServer = data['runQueryServer']
            thisConfig.runRconServer = data['runRconServer']
            thisConfig.safeScripts = data['safeScripts']
            thisConfig.scriptInstructionLimit = data['scriptInstructionLimit']
            thisConfig.scriptInstructionMeasureInterval = data['scriptInstructionMeasureInterval']
            thisConfig.scriptProfilingEnabled = data['scriptProfilingEnabled']
            thisConfig.scriptRecursionLimit = data['scriptRecursionLimit']
            thisConfig.serverFidelity = data['serverFidelity']
            thisConfig.serverName = data['serverName']
            thisConfig.serverOverrideAssetsDigest = data['serverOverrideAssetsDigest']
            thisConfig.tutorialMessages = data['tutorialMessages']
            return thisConfig

    except Exception as e:
        print  'Error reading config: ' + repr(e)

def createConfig():
    pass

def saveConfig():
    pass


if os.path.isfile(configFile):
    config = readConfig()