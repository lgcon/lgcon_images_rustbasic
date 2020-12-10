
import os
# Check env variables
LGC_INSTANCE_NAME = os.environ['LGC_INSTANCE_NAME']
LGC_GAME = os.environ['LGC_GAME']

LGC_RUST_SERVER_IP = os.environ['LGC_RUST_SERVER_IP']
LGC_RUST_SERVER_PORT = os.environ['LGC_RUST_SERVER_PORT']
LGC_RUST_RCON_IP = os.environ['LGC_RUST_RCON_IP']
LGC_RUST_RCON_WEB = os.environ['LGC_RUST_RCON_WEB']
LGC_RUST_SERVER_TICKRATE = os.environ['LGC_RUST_SERVER_TICKRATE']
LGC_RUST_HOSTNAME = os.environ['LGC_RUST_HOSTNAME']
LGC_RUST_IDENTITY = os.environ['LGC_RUST_IDENTITY']
LGC_RUST_MAXPLAYERS = os.environ['LGC_RUST_MAXPLAYERS']

LGC_RUST_CUSTOMMAP_TOGGLE = os.environ['LGC_RUST_CUSTOMMAP_TOGGLE']
LGC_RUST_WORLDSIZE = os.environ['LGC_RUST_WORLDSIZE']
LGC_RUST_SERVERURL = os.environ['LGC_RUST_SERVERURL']

LGC_RUST_SERVERSEED = os.environ['LGC_RUST_SERVERSEED']
LGC_RUST_SERVER_SAVEINTERVAL = os.environ['LGC_RUST_SERVER_SAVEINTERVAL']
LGC_RUST_LOGFILE = os.environ['LGC_RUST_LOGFILE']
LGC_RUST_OXIDE_TOGGLE = os.environ['LGC_RUST_OXIDE_TOGGLE']
RUST_OXIDE_UPDATE_ON_BOOT = os.environ['RUST_OXIDE_UPDATE_ON_BOOT']
LGC_RUST_OXIDE_CONFIGURL = os.environ['LGC_RUST_OXIDE_CONFIGURL']


# Install/update steamcmd
exec(open('/lgc/scripts/installers/install_steamcmd.py').read())



# Check if Oxide is enabled


	# Next check if Oxide doesn't' exist, or if we want to always update it

	# If necessary, download and install latest Oxide




# Add RCON support if necessary

		# Fix the webrcon (customizes a few elements)


		# Start nginx (in the background)




# Start the scheduler (only if update checking is enabled)

# Run the server
# echo "Starting Rust.."
# if [ "$RUST_SERVER_PORT" != "" ]; then
# 	RUST_SERVER_PORT="+server.port $RUST_SERVER_PORT"
# fi
# if [ "$LOGROTATE_ENABLED" = "1" ]; then
# 	unbuffer /steamcmd/rust/RustDedicated $RUST_STARTUP_COMMAND "$RUST_SERVER_PORT" +server.identity "$RUST_SERVER_IDENTITY" +server.seed "$RUST_SERVER_SEED" +server.hostname "$RUST_SERVER_NAME" +server.url "$RUST_SERVER_URL" +server.headerimage "$RUST_SERVER_BANNER_URL" +server.description "$RUST_SERVER_DESCRIPTION" +server.worldsize "$RUST_SERVER_WORLDSIZE" +server.maxplayers "$RUST_SERVER_MAXPLAYERS" +server.saveinterval "$RUST_SERVER_SAVE_INTERVAL" +app.port "$RUST_APP_PORT" 2>&1 | grep --line-buffered -Ev '^\s*$|Filename' | tee $RUST_SERVER_LOG_FILE &
# elif [ "$STDLOG_ENABLED" = "1" ]; then
# 	/steamcmd/rust/RustDedicated $RUST_STARTUP_COMMAND "$RUST_SERVER_PORT" +server.identity "$RUST_SERVER_IDENTITY" +server.seed "$RUST_SERVER_SEED" +server.hostname "$RUST_SERVER_NAME" +server.url "$RUST_SERVER_URL" +server.headerimage "$RUST_SERVER_BANNER_URL" +server.description "$RUST_SERVER_DESCRIPTION" +server.worldsize "$RUST_SERVER_WORLDSIZE" +server.maxplayers "$RUST_SERVER_MAXPLAYERS" +server.saveinterval "$RUST_SERVER_SAVE_INTERVAL" +app.port "$RUST_APP_PORT" 2>&1 &
# else
# 	/steamcmd/rust/RustDedicated $RUST_STARTUP_COMMAND "$RUST_SERVER_PORT" +server.identity "$RUST_SERVER_IDENTITY" +server.seed "$RUST_SERVER_SEED" +server.hostname "$RUST_SERVER_NAME" +server.url "$RUST_SERVER_URL" +server.headerimage "$RUST_SERVER_BANNER_URL" +server.description "$RUST_SERVER_DESCRIPTION" +server.worldsize "$RUST_SERVER_WORLDSIZE" +server.maxplayers "$RUST_SERVER_MAXPLAYERS" +server.saveinterval "$RUST_SERVER_SAVE_INTERVAL" +app.port "$RUST_APP_PORT" &
