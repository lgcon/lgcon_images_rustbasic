ARG VARIANT=focal
FROM mcr.microsoft.com/vscode/devcontainers/base:${VARIANT}

ENV LGC_INSTANCE_NAME="LGC"
ENV LGC_GAME="rust"

ENV LGC_RUST_SERVER_IP="0.0.0.0"
ENV LGC_RUST_SERVER_PORT="28015"
ENV LGC_RUST_RCON_IP="0.0.0.0"
ENV LGC_RUST_RCON_WEB="1"
ENV LGC_RUST_SERVER_TICKRATE="10"
ENV LGC_RUST_HOSTNAME="[ LINUX GAME CONTAINERS ]"
ENV LGC_RUST_IDENTITY="INSTANCE_NAME"
ENV LGC_RUST_MAXPLAYERS="100"

ENV LGC_RUST_CUSTOMMAP_TOGGLE="OFF"
ENV LGC_RUST_WORLDSIZE="3000"
ENV LGC_RUST_SERVERURL="url"
ENV LGC_RUST_SERVERSEED="50000"
ENV LGC_RUST_SERVER_SAVEINTERVAL="600"
ENV LGC_RUST_RCONPASSWORD="lgc"
ENV LGC_RUST_LOGFILE="${LGC_INSTANCE_NAME}.txt"

ENV LGC_RUST_OXIDE_TOGGLE="1"
ENV RUST_OXIDE_UPDATE_ON_BOOT='1'
ENV LGC_RUST_OXIDE_CONFIGURL="url"

ARG DEPENDS_SYS="lib32gcc1 libstdc++6 curl git locales locales-all python3 python3-pip git"
ARG DEPENDS_STEAMCMD="libcurl4-openssl-dev:i386"
ARG URL_STEAMCMD="http://media.steampowered.com/installer/steamcmd_linux.tar.gz"

# Update system
RUN apt-get update -y
RUN apt-get upgrade -y

# Install dependencies
RUN apt-get install -y --no-install-recommends ${DEPENDS_SYS}

# Fix issues with curl and steamcmd
RUN apt-get install --reinstall ca-certificates -y
RUN dpkg --add-architecture i386 && apt-get update -y
RUN apt-get install -y --no-install-recommends ${DEPENDS_STEAMCMD}
RUN ls -la /usr/lib/*/libcurl.so*
RUN ln -sf /usr/lib/i386-linux-gnu/libcurl.so.4 /usr/lib/i386-linux-gnu/libcurl.so
RUN ln -sf /usr/lib/i386-linux-gnu/libcurl.so.4 /usr/lib/i386-linux-gnu/libcurl.so.3

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*

# Install steamcmd
RUN mkdir -p /steamcmd && curl -s ${URL_STEAMCMD} | tar -v -C /steamcmd -zx
RUN chmod +x /steamcmd/steamcmd.sh

# Install game
RUN /steamcmd/steamcmd.sh +login anonymous +force_install_dir /game/ +app_update 258550 +quit

RUN mkdir /lgc
RUN git clone https://github.com/lgcon/lgcon_images_rustbasic.git /lgc/

# Permissions
RUN chmod -R +x /lgc

RUN chown -R vscode /lgc
RUN chown -R vscode /steamcmd/
RUN chown -R vscode /game/

# PORTS
EXPOSE 8080
EXPOSE 28015
EXPOSE 28016
EXPOSE 28082

# ENTRYPOINT [ " /lgc/scripts/entrypoint.py" ]