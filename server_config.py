import json

configFile = "starbound_server.config"



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
    try:
        with open(configFile) as data_file:
            data = json.load(data_file)
            allowAdminCommands =  data['allowAdminCommands']
            print "allowAdminCommands = " + str(allowAdminCommands)

    except Exception as e:
        print  'Error reading config: ' + repr(e)

def createConfig():
    pass

def saveConfig():
    pass


