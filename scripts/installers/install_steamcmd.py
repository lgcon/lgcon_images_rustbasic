import os

dependencies = 'lib32gcc1 libstdc++6'
dependencies_steamcmd = 'libcurl4-openssl-dev:i386'
url_steamcmd = 'http://media.steampowered.com/installer/steamcmd_linux.tar.gz'

# Install dependencies
os.system('apt-get update')
os.system(f'apt-get install -y --no-install-recommends {dependencies}')
os.system('apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*')

# Fix issues with libcurl and steamcmd
os.system('dpkg --add-architecture i386 && apt-get update')
os.system(f'apt-get install -y --no-install-recommends {dependencies_steamcmd}')

os.system('ls -la /usr/lib/*/libcurl.so*')
os.system('ln -sf /usr/lib/i386-linux-gnu/libcurl.so.4 /usr/lib/i386-linux-gnu/libcurl.so')
os.system('ln -sf /usr/lib/i386-linux-gnu/libcurl.so.4 /usr/lib/i386-linux-gnu/libcurl.so.3')
os.system('apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*')

# Install steamcmd and verify that it is working
os.system(f'mkdir -p /steamcmd && curl -s {url_steamcmd} | tar -v -C /steamcmd -zx')
os.system('sudo chmod +x /steamcmd/steamcmd.sh && /steamcmd/steamcmd.sh +login anonymous +quit')