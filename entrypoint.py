# Check env variables
os.environ['HOME'])


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
echo "Starting Rust.."
if [ "$RUST_SERVER_PORT" != "" ]; then
	RUST_SERVER_PORT="+server.port $RUST_SERVER_PORT"
fi
if [ "$LOGROTATE_ENABLED" = "1" ]; then
	unbuffer /steamcmd/rust/RustDedicated $RUST_STARTUP_COMMAND "$RUST_SERVER_PORT" +server.identity "$RUST_SERVER_IDENTITY" +server.seed "$RUST_SERVER_SEED" +server.hostname "$RUST_SERVER_NAME" +server.url "$RUST_SERVER_URL" +server.headerimage "$RUST_SERVER_BANNER_URL" +server.description "$RUST_SERVER_DESCRIPTION" +server.worldsize "$RUST_SERVER_WORLDSIZE" +server.maxplayers "$RUST_SERVER_MAXPLAYERS" +server.saveinterval "$RUST_SERVER_SAVE_INTERVAL" +app.port "$RUST_APP_PORT" 2>&1 | grep --line-buffered -Ev '^\s*$|Filename' | tee $RUST_SERVER_LOG_FILE &
elif [ "$STDLOG_ENABLED" = "1" ]; then
	/steamcmd/rust/RustDedicated $RUST_STARTUP_COMMAND "$RUST_SERVER_PORT" +server.identity "$RUST_SERVER_IDENTITY" +server.seed "$RUST_SERVER_SEED" +server.hostname "$RUST_SERVER_NAME" +server.url "$RUST_SERVER_URL" +server.headerimage "$RUST_SERVER_BANNER_URL" +server.description "$RUST_SERVER_DESCRIPTION" +server.worldsize "$RUST_SERVER_WORLDSIZE" +server.maxplayers "$RUST_SERVER_MAXPLAYERS" +server.saveinterval "$RUST_SERVER_SAVE_INTERVAL" +app.port "$RUST_APP_PORT" 2>&1 &
else
	/steamcmd/rust/RustDedicated $RUST_STARTUP_COMMAND "$RUST_SERVER_PORT" +server.identity "$RUST_SERVER_IDENTITY" +server.seed "$RUST_SERVER_SEED" +server.hostname "$RUST_SERVER_NAME" +server.url "$RUST_SERVER_URL" +server.headerimage "$RUST_SERVER_BANNER_URL" +server.description "$RUST_SERVER_DESCRIPTION" +server.worldsize "$RUST_SERVER_WORLDSIZE" +server.maxplayers "$RUST_SERVER_MAXPLAYERS" +server.saveinterval "$RUST_SERVER_SAVE_INTERVAL" +app.port "$RUST_APP_PORT" &
