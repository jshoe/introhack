Last login: Fri Jul 18 17:58:06 on ttys000
Jonathans-MacBook-Pro:IntroHackathon jonathan$ ls
Jonathans-MacBook-Pro:IntroHackathon jonathan$ cd ..
Jonathans-MacBook-Pro:Desktop jonathan$ cd ..
Jonathans-MacBook-Pro:~ jonathan$ ls
2014-07-18key		Documents		Music
2014-07-18key.pub	Downloads		Pictures
Applications		Library			Public
Desktop			Movies
Jonathans-MacBook-Pro:~ jonathan$ mkdir .ssh
mkdir: .ssh: File exists
Jonathans-MacBook-Pro:~ jonathan$ cd .ssh
Jonathans-MacBook-Pro:.ssh jonathan$ ls
known_hosts
Jonathans-MacBook-Pro:.ssh jonathan$ cd ..
Jonathans-MacBook-Pro:~ jonathan$ ls
2014-07-18key		Documents		Music
2014-07-18key.pub	Downloads		Pictures
Applications		Library			Public
Desktop			Movies
Jonathans-MacBook-Pro:~ jonathan$ mv 2014-07-18key .ssh
Jonathans-MacBook-Pro:~ jonathan$ mv 2014-07-18key.pub .ssh
Jonathans-MacBook-Pro:~ jonathan$ ls
Applications	Documents	Library		Music		Public
Desktop		Downloads	Movies		Pictures
Jonathans-MacBook-Pro:~ jonathan$ cd .ssh
Jonathans-MacBook-Pro:.ssh jonathan$ ls
2014-07-18key		2014-07-18key.pub	known_hosts
Jonathans-MacBook-Pro:.ssh jonathan$ 
Display all 1432 possibilities? (y or n)
!                            mkextunpack
./                           mkfifo
2to3                         mkfile
2to3-                        mklocale
2to3-2.7                     mknod
2to32.6                      mkpassdb
:                            mktemp
AppleFileServer              mmroff
BootCacheControl             mnthome
BuildStrings                 moose-outdated
CpMac                        moose-outdated5.12
DeRez                        moose-outdated5.16
DevToolsSecurity             more
DirectoryService             mount
FileStatsAgent               mount_acfs
GetFileInfo                  mount_afp
KernelEventAgent             mount_cd9660
Kobil_mIDentity_switch       mount_cddafs
MergePef                     mount_devfs
MvMac                        mount_exfat
NetBootClientStatus          mount_fdesc
PasswordService              mount_ftp
RSA_SecurID_getpasswd        mount_hfs
Jonathans-MacBook-Pro:.ssh jonathan$ 
Jonathans-MacBook-Pro:.ssh jonathan$ 
Jonathans-MacBook-Pro:.ssh jonathan$ 
Jonathans-MacBook-Pro:.ssh jonathan$ ls -al ~/.ssh
total 24
drwx------   5 jonathan  staff   170 Jul 18 18:05 .
drwxr-xr-x+ 17 jonathan  staff   578 Jul 18 18:05 ..
-rw-------   1 jonathan  staff  1679 Jul 18 17:41 2014-07-18key
-rw-r--r--   1 jonathan  staff   401 Jul 18 17:41 2014-07-18key.pub
-rw-r--r--   1 jonathan  staff  1199 Jul 18 18:06 known_hosts
Jonathans-MacBook-Pro:.ssh jonathan$ pbcopy < 2014-07-18key.pub
Jonathans-MacBook-Pro:.ssh jonathan$ ssh -T git@github.com
Permission denied (publickey).
Jonathans-MacBook-Pro:.ssh jonathan$ ls
2014-07-18key		2014-07-18key.pub	known_hosts
Jonathans-MacBook-Pro:.ssh jonathan$ ssh-keygen -t rsa -C "portdevil@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/jonathan/.ssh/id_rsa): testkey
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in testkey.
Your public key has been saved in testkey.pub.
The key fingerprint is:
3d:2d:49:57:e3:56:c5:14:c7:6a:c2:65:53:a0:8e:26 portdevil@gmail.com
The key's randomart image is:
+--[ RSA 2048]----+
|              +BO|
|             ++o+|
|          ..oooo |
|         o *o.o  |
|        E B oo   |
|         o o     |
|                 |
|                 |
|                 |
+-----------------+
Jonathans-MacBook-Pro:.ssh jonathan$ eval "$(ssh-agent -s)"
Agent pid 3713
Jonathans-MacBook-Pro:.ssh jonathan$ pbcopy < ~/.ssh/id_rsa.pub
-bash: /Users/jonathan/.ssh/id_rsa.pub: No such file or directory
Jonathans-MacBook-Pro:.ssh jonathan$ pbcopy < ~/.ssh/testkey
testkey      testkey.pub  
Jonathans-MacBook-Pro:.ssh jonathan$ pbcopy < ~/.ssh/testkey
testkey      testkey.pub  
Jonathans-MacBook-Pro:.ssh jonathan$ pbcopy < ~/.ssh/testkey
testkey      testkey.pub  
Jonathans-MacBook-Pro:.ssh jonathan$ pbcopy < ~/.ssh/testkey
testkey      testkey.pub  
Jonathans-MacBook-Pro:.ssh jonathan$ pbcopy < ~/.ssh/testkey.pub
Jonathans-MacBook-Pro:.ssh jonathan$ ls
2014-07-18key		known_hosts		testkey.pub
2014-07-18key.pub	testkey
Jonathans-MacBook-Pro:.ssh jonathan$ ssh -T git@github.com
Warning: Permanently added the RSA host key for IP address '192.30.252.131' to the list of known hosts.
Permission denied (publickey).
Jonathans-MacBook-Pro:.ssh jonathan$ ls
2014-07-18key		known_hosts		testkey.pub
2014-07-18key.pub	testkey
Jonathans-MacBook-Pro:.ssh jonathan$ ssh-add 
2014-07-18key      known_hosts        testkey.pub        
2014-07-18key.pub  testkey            
Jonathans-MacBook-Pro:.ssh jonathan$ ssh-add testkey.pub
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for 'testkey.pub' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Jonathans-MacBook-Pro:.ssh jonathan$ ls
2014-07-18key		known_hosts		testkey.pub
2014-07-18key.pub	testkey
Jonathans-MacBook-Pro:.ssh jonathan$ ssh-keygen -t rsa -C "portdevil@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/jonathan/.ssh/id_rsa): 2014-07-18key2
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in 2014-07-18key2.
Your public key has been saved in 2014-07-18key2.pub.
The key fingerprint is:
96:10:23:5e:34:a0:ef:0b:a2:a4:72:04:fc:f6:5e:79 portdevil@gmail.com
The key's randomart image is:
+--[ RSA 2048]----+
|    oo*          |
|   o o +         |
|. . . .          |
|.. .   . .       |
| .. .   S        |
|  .+   ..        |
|.oo o  o E       |
|=... o. .        |
|+.  o.           |
+-----------------+
Jonathans-MacBook-Pro:.ssh jonathan$ ls
2014-07-18key		2014-07-18key2.pub	testkey.pub
2014-07-18key.pub	known_hosts
2014-07-18key2		testkey
Jonathans-MacBook-Pro:.ssh jonathan$ eval "$(ssh-agent -s)"
Agent pid 3781
Jonathans-MacBook-Pro:.ssh jonathan$ ssh-add ~/.ssh/2014-07-18key2
Enter passphrase for /Users/jonathan/.ssh/2014-07-18key2: 
Identity added: /Users/jonathan/.ssh/2014-07-18key2 (/Users/jonathan/.ssh/2014-07-18key2)
Jonathans-MacBook-Pro:.ssh jonathan$ ls
2014-07-18key		2014-07-18key2.pub	testkey.pub
2014-07-18key.pub	known_hosts
2014-07-18key2		testkey
Jonathans-MacBook-Pro:.ssh jonathan$ ls
2014-07-18key		2014-07-18key2.pub	testkey.pub
2014-07-18key.pub	known_hosts
2014-07-18key2		testkey
Jonathans-MacBook-Pro:.ssh jonathan$ pbcopy < ~/.ssh/
2014-07-18key       2014-07-18key2.pub  testkey.pub
2014-07-18key.pub   known_hosts         
2014-07-18key2      testkey             
Jonathans-MacBook-Pro:.ssh jonathan$ pbcopy < ~/.ssh/
2014-07-18key       2014-07-18key2.pub  testkey.pub
2014-07-18key.pub   known_hosts         
2014-07-18key2      testkey             
Jonathans-MacBook-Pro:.ssh jonathan$ pbcopy < ~/.ssh/2014-07-18key.pub
Jonathans-MacBook-Pro:.ssh jonathan$ pbcopy < ~/.ssh/2014-07-18key2.pub
Jonathans-MacBook-Pro:.ssh jonathan$ ls
2014-07-18key		2014-07-18key2.pub	testkey.pub
2014-07-18key.pub	known_hosts
2014-07-18key2		testkey
Jonathans-MacBook-Pro:.ssh jonathan$ ssh -T git@github.com
Hi portdevil! You've successfully authenticated, but GitHub does not provide shell access.
Jonathans-MacBook-Pro:.ssh jonathan$ git clone git@github.com:portdevil/introhack.git
Cloning into 'introhack'...
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 6 (delta 0), reused 3 (delta 0)
Receiving objects: 100% (6/6), done.
Checking connectivity... done.
Jonathans-MacBook-Pro:.ssh jonathan$ ls
2014-07-18key		2014-07-18key2.pub	testkey
2014-07-18key.pub	introhack		testkey.pub
2014-07-18key2		known_hosts
Jonathans-MacBook-Pro:.ssh jonathan$ rm introhack
rm: introhack: is a directory
Jonathans-MacBook-Pro:.ssh jonathan$ rm -r introhack
override r--r--r--  jonathan/staff for introhack/.git/objects/pack/pack-d2c1f86de6d47a903a3827c778441a2ddc971fde.idx? ^C
Jonathans-MacBook-Pro:.ssh jonathan$ ls
2014-07-18key		2014-07-18key2.pub	testkey
2014-07-18key.pub	introhack		testkey.pub
2014-07-18key2		known_hosts
Jonathans-MacBook-Pro:.ssh jonathan$  cd ..
Jonathans-MacBook-Pro:~ jonathan$ cd ..
Jonathans-MacBook-Pro:Users jonathan$ ls
Shared		jonathan
Jonathans-MacBook-Pro:Users jonathan$ cd jonathan/
Jonathans-MacBook-Pro:~ jonathan$ ls
Applications	Documents	Library		Music		Public
Desktop		Downloads	Movies		Pictures
Jonathans-MacBook-Pro:~ jonathan$ cd Desktop/
Jonathans-MacBook-Pro:Desktop jonathan$ ls
IntroHackathon
Jonathans-MacBook-Pro:Desktop jonathan$ git clone git@github.com:portdevil/introhack.git
Cloning into 'introhack'...
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 6 (delta 0), reused 3 (delta 0)
Receiving objects: 100% (6/6), done.
Checking connectivity... done.
Jonathans-MacBook-Pro:Desktop jonathan$ ls
IntroHackathon	introhack
Jonathans-MacBook-Pro:Desktop jonathan$ cd introhack/
Jonathans-MacBook-Pro:introhack jonathan$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

nothing to commit, working directory clean
Jonathans-MacBook-Pro:introhack jonathan$ ls
README.md
Jonathans-MacBook-Pro:introhack jonathan$ ls
README.md
Jonathans-MacBook-Pro:introhack jonathan$ python3 --version
-bash: python3: command not found
Jonathans-MacBook-Pro:introhack jonathan$ ls
README.md
Jonathans-MacBook-Pro:introhack jonathan$ python
Python 2.7.5 (default, Mar  9 2014, 22:15:05) 
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> ^D
Jonathans-MacBook-Pro:introhack jonathan$ python --version
Python 2.7.5
Jonathans-MacBook-Pro:introhack jonathan$ ls
README.md
Jonathans-MacBook-Pro:introhack jonathan$ brew
-bash: brew: command not found
Jonathans-MacBook-Pro:introhack jonathan$ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
==> This script will install:
/usr/local/bin/brew
/usr/local/Library/...
/usr/local/share/man/man1/brew.1

Press RETURN to continue or any other key to abort
==> /usr/bin/sudo /bin/mkdir /usr/local
Password:
==> /usr/bin/sudo /bin/chmod g+rwx /usr/local
==> /usr/bin/sudo /usr/bin/chgrp admin /usr/local
==> /usr/bin/sudo /bin/mkdir /Library/Caches/Homebrew
==> /usr/bin/sudo /bin/chmod g+rwx /Library/Caches/Homebrew
==> Downloading and installing Homebrew...
remote: Counting objects: 186405, done.
remote: Compressing objects: 100% (51092/51092), done.
remote: Total 186405 (delta 134201), reused 186326 (delta 134144)
Receiving objects: 100% (186405/186405), 36.98 MiB | 1.94 MiB/s, done.
Resolving deltas: 100% (134201/134201), done.
From https://github.com/Homebrew/homebrew
 * [new branch]      master     -> origin/master
HEAD is now at f12a030 arangodb: update 2.2.0 bottle.
==> Installation successful!
==> Next steps
Run `brew doctor` before you install anything
Run `brew help` to get started
Jonathans-MacBook-Pro:introhack jonathan$ brew doctor
Your system is ready to brew.
Jonathans-MacBook-Pro:introhack jonathan$ brew install python3
==> Installing dependencies for python3: readline, sqlite, gdbm, openssl, xz
==> Installing python3 dependency: readline
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/readline-6.3.6.mavericks.bottle.tar.gz
######################################################################## 100.0%
==> Pouring readline-6.3.6.mavericks.bottle.tar.gz
==> Caveats
This formula is keg-only, so it was not symlinked into /usr/local.

OS X provides the BSD libedit library, which shadows libreadline.
In order to prevent conflicts when programs look for libreadline we are
defaulting this GNU Readline installation to keg-only.

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/readline/lib
    CPPFLAGS: -I/usr/local/opt/readline/include

==> Summary
🍺  /usr/local/Cellar/readline/6.3.6: 40 files, 2.1M
==> Installing python3 dependency: sqlite
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/sqlite-3.8.5.mavericks.bottle.tar.gz
######################################################################## 100.0%
==> Pouring sqlite-3.8.5.mavericks.bottle.tar.gz
==> Caveats
This formula is keg-only, so it was not symlinked into /usr/local.

Mac OS X already provides this software and installing another version in
parallel can cause all kinds of trouble.

OS X provides an older sqlite3.

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/sqlite/lib
    CPPFLAGS: -I/usr/local/opt/sqlite/include

==> Summary
🍺  /usr/local/Cellar/sqlite/3.8.5: 9 files, 2.1M
==> Installing python3 dependency: gdbm
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/gdbm-1.11.mavericks.bottle.tar.gz
######################################################################## 100.0%
==> Pouring gdbm-1.11.mavericks.bottle.tar.gz
🍺  /usr/local/Cellar/gdbm/1.11: 16 files, 408K
==> Installing python3 dependency: openssl
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/openssl-1.0.1h.mavericks.bottle.tar.gz
######################################################################## 100.0%
==> Pouring openssl-1.0.1h.mavericks.bottle.tar.gz
==> Caveats
A CA file has been bootstrapped using certificates from the system
keychain. To add additional certificates, place .pem files in
  /usr/local/etc/openssl/certs

and run
  /usr/local/opt/openssl/bin/c_rehash

This formula is keg-only, so it was not symlinked into /usr/local.

Mac OS X already provides this software and installing another version in
parallel can cause all kinds of trouble.

The OpenSSL provided by OS X is too old for some software.

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/openssl/lib
    CPPFLAGS: -I/usr/local/opt/openssl/include

==> Summary
🍺  /usr/local/Cellar/openssl/1.0.1h: 429 files, 14M
==> Installing python3 dependency: xz
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/xz-5.0.5.mavericks.bottle.3.tar.gz
######################################################################## 100.0%
==> Pouring xz-5.0.5.mavericks.bottle.3.tar.gz
🍺  /usr/local/Cellar/xz/5.0.5: 58 files, 1.5M
==> Installing python3
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/python3-3.4.1.mavericks.bottle.tar.gz
######################################################################## 100.0%
==> Pouring python3-3.4.1.mavericks.bottle.tar.gz
==> Caveats
Pip has been installed. To update it
  pip3 install --upgrade pip

You can install Python packages with
  pip3 install <package>

They will install into the site-package directory
  /usr/local/lib/python3.4/site-packages

See: https://github.com/Homebrew/homebrew/wiki/Homebrew-and-Python

.app bundles were installed.
Run `brew linkapps` to symlink these to /Applications.
==> /usr/local/Cellar/python3/3.4.1/bin/python3 -m ensurepip --upgrade
==> Summary
🍺  /usr/local/Cellar/python3/3.4.1: 3845 files, 66M
Jonathans-MacBook-Pro:introhack jonathan$ ls
README.md
Jonathans-MacBook-Pro:introhack jonathan$ pip3 install flask
Downloading/unpacking flask
  Downloading Flask-0.10.1.tar.gz (544kB): 544kB downloaded
  Running setup.py (path:/private/var/folders/0p/2tpy5vsj6nx9pg8gnnb1z4vw0000gn/T/pip_build_jonathan/flask/setup.py) egg_info for package flask
    
    warning: no files found matching '*' under directory 'tests'
    warning: no previously-included files matching '*.pyc' found under directory 'docs'
    warning: no previously-included files matching '*.pyo' found under directory 'docs'
    warning: no previously-included files matching '*.pyc' found under directory 'tests'
    warning: no previously-included files matching '*.pyo' found under directory 'tests'
    warning: no previously-included files matching '*.pyc' found under directory 'examples'
    warning: no previously-included files matching '*.pyo' found under directory 'examples'
    no previously-included directories found matching 'docs/_build'
    no previously-included directories found matching 'docs/_themes/.git'
Downloading/unpacking Werkzeug>=0.7 (from flask)
  Downloading Werkzeug-0.9.6.tar.gz (1.1MB): 1.1MB downloaded
  Running setup.py (path:/private/var/folders/0p/2tpy5vsj6nx9pg8gnnb1z4vw0000gn/T/pip_build_jonathan/Werkzeug/setup.py) egg_info for package Werkzeug
    
    warning: no files found matching '*' under directory 'werkzeug/debug/templates'
    warning: no files found matching '*' under directory 'tests'
    warning: no previously-included files matching '*.pyc' found under directory 'docs'
    warning: no previously-included files matching '*.pyo' found under directory 'docs'
    warning: no previously-included files matching '*.pyc' found under directory 'tests'
    warning: no previously-included files matching '*.pyo' found under directory 'tests'
    warning: no previously-included files matching '*.pyc' found under directory 'examples'
    warning: no previously-included files matching '*.pyo' found under directory 'examples'
    no previously-included directories found matching 'docs/_build'
Downloading/unpacking Jinja2>=2.4 (from flask)
  Downloading Jinja2-2.7.3.tar.gz (378kB): 378kB downloaded
  Running setup.py (path:/private/var/folders/0p/2tpy5vsj6nx9pg8gnnb1z4vw0000gn/T/pip_build_jonathan/Jinja2/setup.py) egg_info for package Jinja2
    
    warning: no files found matching '*' under directory 'custom_fixers'
    warning: no previously-included files matching '*' found under directory 'docs/_build'
    warning: no previously-included files matching '*.pyc' found under directory 'jinja2'
    warning: no previously-included files matching '*.pyc' found under directory 'docs'
    warning: no previously-included files matching '*.pyo' found under directory 'jinja2'
    warning: no previously-included files matching '*.pyo' found under directory 'docs'
Downloading/unpacking itsdangerous>=0.21 (from flask)
  Downloading itsdangerous-0.24.tar.gz (46kB): 46kB downloaded
  Running setup.py (path:/private/var/folders/0p/2tpy5vsj6nx9pg8gnnb1z4vw0000gn/T/pip_build_jonathan/itsdangerous/setup.py) egg_info for package itsdangerous
    
    warning: no previously-included files matching '*' found under directory 'docs/_build'
Downloading/unpacking markupsafe (from Jinja2>=2.4->flask)
  Downloading MarkupSafe-0.23.tar.gz
  Running setup.py (path:/private/var/folders/0p/2tpy5vsj6nx9pg8gnnb1z4vw0000gn/T/pip_build_jonathan/markupsafe/setup.py) egg_info for package markupsafe
    
Installing collected packages: flask, Werkzeug, Jinja2, itsdangerous, markupsafe
  Running setup.py install for flask
    
    warning: no files found matching '*' under directory 'tests'
    warning: no previously-included files matching '*.pyc' found under directory 'docs'
    warning: no previously-included files matching '*.pyo' found under directory 'docs'
    warning: no previously-included files matching '*.pyc' found under directory 'tests'
    warning: no previously-included files matching '*.pyo' found under directory 'tests'
    warning: no previously-included files matching '*.pyc' found under directory 'examples'
    warning: no previously-included files matching '*.pyo' found under directory 'examples'
    no previously-included directories found matching 'docs/_build'
    no previously-included directories found matching 'docs/_themes/.git'
  Running setup.py install for Werkzeug
    
    warning: no files found matching '*' under directory 'werkzeug/debug/templates'
    warning: no files found matching '*' under directory 'tests'
    warning: no previously-included files matching '*.pyc' found under directory 'docs'
    warning: no previously-included files matching '*.pyo' found under directory 'docs'
    warning: no previously-included files matching '*.pyc' found under directory 'tests'
    warning: no previously-included files matching '*.pyo' found under directory 'tests'
    warning: no previously-included files matching '*.pyc' found under directory 'examples'
    warning: no previously-included files matching '*.pyo' found under directory 'examples'
    no previously-included directories found matching 'docs/_build'
  Running setup.py install for Jinja2
    
    warning: no files found matching '*' under directory 'custom_fixers'
    warning: no previously-included files matching '*' found under directory 'docs/_build'
    warning: no previously-included files matching '*.pyc' found under directory 'jinja2'
    warning: no previously-included files matching '*.pyc' found under directory 'docs'
    warning: no previously-included files matching '*.pyo' found under directory 'jinja2'
    warning: no previously-included files matching '*.pyo' found under directory 'docs'
  Running setup.py install for itsdangerous
    
    warning: no previously-included files matching '*' found under directory 'docs/_build'
  Running setup.py install for markupsafe
    
    building 'markupsafe._speedups' extension
    clang -Wno-unused-result -Werror=declaration-after-statement -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/usr/local/include -I/usr/local/opt/sqlite/include -I/usr/local/Cellar/python3/3.4.1/Frameworks/Python.framework/Versions/3.4/include/python3.4m -c markupsafe/_speedups.c -o build/temp.macosx-10.9-x86_64-3.4/markupsafe/_speedups.o
    clang -bundle -undefined dynamic_lookup -L/usr/local/lib -L/usr/local/opt/sqlite/lib build/temp.macosx-10.9-x86_64-3.4/markupsafe/_speedups.o -o build/lib.macosx-10.9-x86_64-3.4/markupsafe/_speedups.so
Successfully installed flask Werkzeug Jinja2 itsdangerous markupsafe
Cleaning up...
Jonathans-MacBook-Pro:introhack jonathan$ ls
README.md
Jonathans-MacBook-Pro:introhack jonathan$ ls
README.md
Jonathans-MacBook-Pro:introhack jonathan$ ls
README.md
Jonathans-MacBook-Pro:introhack jonathan$ vim main.py
Jonathans-MacBook-Pro:introhack jonathan$ git add main.py
Jonathans-MacBook-Pro:introhack jonathan$ ls
README.md	main.py
Jonathans-MacBook-Pro:introhack jonathan$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   main.py

Jonathans-MacBook-Pro:introhack jonathan$ git add -A
Jonathans-MacBook-Pro:introhack jonathan$ git commit -a -m "made the main file"
[master 804995d] made the main file
 Committer: Jonathan Sheu <jonathan@Jonathans-MacBook-Pro.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
 create mode 100644 main.py
Jonathans-MacBook-Pro:introhack jonathan$ git config --global portdevil "portdevil"
error: key does not contain a section: portdevil
Jonathans-MacBook-Pro:introhack jonathan$ git config --global user.name "portdevil"
Jonathans-MacBook-Pro:introhack jonathan$ git config --global user.email portdevil@gmail.com
Jonathans-MacBook-Pro:introhack jonathan$ git commit -a -m "made the main file"
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working directory clean
Jonathans-MacBook-Pro:introhack jonathan$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 291 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To git@github.com:portdevil/introhack.git
   d4d3878..804995d  master -> master
Jonathans-MacBook-Pro:introhack jonathan$ cat main.py

Jonathans-MacBook-Pro:introhack jonathan$ vim main.py
Jonathans-MacBook-Pro:introhack jonathan$ python main.py
Jonathans-MacBook-Pro:introhack jonathan$ vim main.py
Jonathans-MacBook-Pro:introhack jonathan$ python main.py

Hello, and welcome to the game.
Please enter your name:
Jonathan
Traceback (most recent call last):
  File "main.py", line 7, in <module>
    main()
  File "main.py", line 2, in main
    user_name = input("\nHello, and welcome to the game.\nPlease enter your name:\n")
  File "<string>", line 1, in <module>
NameError: name 'Jonathan' is not defined
Jonathans-MacBook-Pro:introhack jonathan$ vim main.py
Jonathans-MacBook-Pro:introhack jonathan$ python main.py

Hello, and welcome to the game.
Please enter your name:
Jonathan
Traceback (most recent call last):
  File "main.py", line 7, in <module>
    main()
  File "main.py", line 2, in main
    user_name = input("\nHello, and welcome to the game.\nPlease enter your name:\n")
  File "<string>", line 1, in <module>
NameError: name 'Jonathan' is not defined
Jonathans-MacBook-Pro:introhack jonathan$ vim main.py
Jonathans-MacBook-Pro:introhack jonathan$ cat main.py
def main():
    user_name = input('\nHello, and welcome to the game.\nPlease enter your name:\n')
    print("\nHello " + user_name + "!")

    return

def start_scene():
    print("start text")

def user_death():
    print("You have died and failed. Goodbye.")
    return

def user_success():
    print("You have beat the game! Congratulations! Enjoy the rest of your day.")

main()
Jonathans-MacBook-Pro:introhack jonathan$ git push
Everything up-to-date
Jonathans-MacBook-Pro:introhack jonathan$ git add -a
error: unknown switch `a'
usage: git add [options] [--] <pathspec>...

    -n, --dry-run         dry run
    -v, --verbose         be verbose

    -i, --interactive     interactive picking
    -p, --patch           select hunks interactively
    -e, --edit            edit current diff and apply
    -f, --force           allow adding otherwise ignored files
    -u, --update          update tracked files
    -N, --intent-to-add   record only the fact that the path will be added later
    -A, --all             add changes from all tracked and untracked files
    --ignore-removal      ignore paths removed in the working tree (same as --no-all)
    --refresh             don't add, only refresh the index
    --ignore-errors       just skip files which cannot be added because of errors
    --ignore-missing      check if - even missing - files are ignored in dry run

Jonathans-MacBook-Pro:introhack jonathan$ git add -A
Jonathans-MacBook-Pro:introhack jonathan$ git commit -a -m "updated"
[master af3d62e] updated
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 .main.py.swp
Jonathans-MacBook-Pro:introhack jonathan$ git push
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 212 bytes | 0 bytes/s, done.
Total 2 (delta 1), reused 0 (delta 0)
To git@github.com:portdevil/introhack.git
   a52dd16..af3d62e  master -> master
Jonathans-MacBook-Pro:introhack jonathan$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

nothing to commit, working directory clean
Jonathans-MacBook-Pro:introhack jonathan$ git pull
remote: Counting objects: 8, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 5 (delta 2), reused 5 (delta 2)
Unpacking objects: 100% (5/5), done.
From github.com:portdevil/introhack
   af3d62e..63b6463  master     -> origin/master
Updating af3d62e..63b6463
Fast-forward
 story | 31 +++++++++++++++++++++++++++----
 1 file changed, 27 insertions(+), 4 deletions(-)
Jonathans-MacBook-Pro:introhack jonathan$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

nothing to commit, working directory clean
Jonathans-MacBook-Pro:introhack jonathan$ cat story 
What is your name?

You've just been assigned your new CS project.
What do you decide to do?
	Start now. (s1)	
	Start Later. (s2)


"AFTER PROJECT"
(squirrel) 
Great! You are on your way to Soda when sUdDenly a wild squiRrel appears!!!
	Feed it. (feed squirrel)
	Kick it. (kick squirrel)
(party) 
Instead of working you decide to go to a party!!
	It's a study party for a class more important than CS... (study party)
	Turnt up!! (turn up)

(feed squirrel)
That squirrel bites you!!
	Bite it back! (bite back)
	Head over to the Tang Center because you forgot to waive SHIP and your health is your number one priority. (tang)
(kick squirrel)
The squirrel thinks you're rood. 
	Continue to Soda.
	All this squirrel kicking makes you tired. You head home for a nap.

(study party)
What?? A class more important CS?? HAHAHA
	Yeah man I was jk!
	I'm delirious and I choose to stay at the study party.
(turn up)
Turn up for WHATT?
	Not your grades!! You failed this class.


Jonathans-MacBook-Pro:introhack jonathan$ 
Jonathans-MacBook-Pro:introhack jonathan$ cat story 
What is your name?

You've just been assigned your new CS project.
What do you decide to do?
	Start now. (s1)	
	Start Later. (s2)


"AFTER PROJECT"
(squirrel) 
Great! You are on your way to Soda when sUdDenly a wild squiRrel appears!!!
	Feed it. (feed squirrel)
	Kick it. (kick squirrel)
(party) 
Instead of working you decide to go to a party!!
	It's a study party for a class more important than CS... (study party)
	Turnt up!! (turn up)

(feed squirrel)
That squirrel bites you!!
	Bite it back! (bite back)
	Head over to the Tang Center because you forgot to waive SHIP and your health is your number one priority. (tang)
(kick squirrel)
The squirrel thinks you're rood. 
	Continue to Soda.
	All this squirrel kicking makes you tired. You head home for a nap.

(study party)
What?? A class more important CS?? HAHAHA
	Yeah man I was jk!
	I'm delirious and I choose to stay at the study party.
(turn up)
Turn up for WHATT?
	Not your grades!! You failed this class.


Jonathans-MacBook-Pro:introhack jonathan$ git pull
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 3 (delta 1)
Unpacking objects: 100% (3/3), done.
From github.com:portdevil/introhack
   63b6463..c27651e  master     -> origin/master
Updating 63b6463..c27651e
Fast-forward
 story | 48 ++++++++++++++++++++++++++++++++++++++++++------
 1 file changed, 42 insertions(+), 6 deletions(-)
Jonathans-MacBook-Pro:introhack jonathan$ cat story 














Jonathans-MacBook-Pro:introhack jonathan$ cat story 
What is your name?

You've just been assigned your new CS project.
What do you decide to do?
	Start now. (squirrel)	
	Start Later. (party)


"AFTER PROJECT"
(squirrel) 
Great! You are on your way to Soda when sUdDenly a wild squiRrel appears!!!
	Feed it. (feed squirrel)
	Kick it. (kick squirrel)
(party) 
Instead of working you decide to go to a party!!
	It's a study party for a class more important than CS... (study party)
	Turnt up!! (turn up)

(feed squirrel)
That squirrel bites you!!
	Bite it back! (bite back)
	Head over to the Tang Center because you forgot to waive SHIP and your health is your number one priority. (tang)
(kick squirrel)
The squirrel thinks you're rood. 
	Continue to Soda. (go to Soda)
	All this squirrel kicking makes you tired. You head home for a nap. (nap)

(study party)
What?? A class more important CS?? HAHAHA
	Yeah man I was jk! (jk)
	I'm delirious and I choose to stay at the study party. (stay)
(turn up)
Turn up for WHATT?
	Not your grades!! You failed this class.
	(GAME OVER)

(bite back)
Yumm... squirrel! 
	You die of salmonella. 
	(GAME OVER)
(tang)
You decide that while you're here, you're going to try to appeal your waiver. You are denied again!
	Flip a table (table)
	Calmly accept your fate (fate)

(jk)
You think this is a joke?!
	Ded. (game over)
(stay)
You fail CS because you're too busy study partying.
	Ded. (game over)

(table)
You are kicked out of Tang and die of infection.
	Ded. (game over)
(fate)
The table flips over anyway. You are kicked out of Tang for disturbing the peace.
	You leave in pieces. (game over)

(go to Soda)
You thought it was due at midnight today. But it was really due midnight yesterday.
	Cry.
	Cry more! (GAME OVER)
(nap)
You oversleep and miss the deadline!
	Cry.
	Creys. (GAME OVER)





Jonathans-MacBook-Pro:introhack jonathan$ cat main.py
def main():
    user_name = input('\nHello, and welcome to the game.\nPlease enter your name:\n')
    print("\nHello " + user_name + "!")
    return

def start_scene():
    print("")

def user_death():
    print("You have died and failed. Goodbye.")
    return

def user_success():
    print("You have beat the game! Congratulations! Enjoy the rest of your day.")

main()
Jonathans-MacBook-Pro:introhack jonathan$ ls
README.md	main.py		story
Jonathans-MacBook-Pro:introhack jonathan$ cat story
What is your name?

You've just been assigned your new CS project.
What do you decide to do?
	Start now. (squirrel)	
	Start Later. (party)


"AFTER PROJECT"
(squirrel) 
Great! You are on your way to Soda when sUdDenly a wild squiRrel appears!!!
	Feed it. (feed squirrel)
	Kick it. (kick squirrel)
(party) 
Instead of working you decide to go to a party!!
	It's a study party for a class more important than CS... (study party)
	Turnt up!! (turn up)

(feed squirrel)
That squirrel bites you!!
	Bite it back! (bite back)
	Head over to the Tang Center because you forgot to waive SHIP and your health is your number one priority. (tang)
(kick squirrel)
The squirrel thinks you're rood. 
	Continue to Soda. (go to Soda)
	All this squirrel kicking makes you tired. You head home for a nap. (nap)

(study party)
What?? A class more important CS?? HAHAHA
	Yeah man I was jk! (jk)
	I'm delirious and I choose to stay at the study party. (stay)
(turn up)
Turn up for WHATT?
	Not your grades!! You failed this class.
	(GAME OVER)

(bite back)
Yumm... squirrel! 
	You die of salmonella. 
	(GAME OVER)
(tang)
You decide that while you're here, you're going to try to appeal your waiver. You are denied again!
	Flip a table (table)
	Calmly accept your fate (fate)

(jk)
You think this is a joke?!
	Ded. (game over)
(stay)
You fail CS because you're too busy study partying.
	Ded. (game over)

(table)
You are kicked out of Tang and die of infection.
	Ded. (game over)
(fate)
The table flips over anyway. You are kicked out of Tang for disturbing the peace.
	You leave in pieces. (game over)

(go to Soda)
You thought it was due at midnight today. But it was really due midnight yesterday.
	Cry.
	Cry more! (GAME OVER)
(nap)
You oversleep and miss the deadline!
	Cry.
	Creys. (GAME OVER)





Jonathans-MacBook-Pro:introhack jonathan$ ls
README.md	main.py		story
Jonathans-MacBook-Pro:introhack jonathan$ cat main.py
def main():
    user_name = input('\nHello, and welcome to the game. Prepare for an adventure!\nLoading game...\nPlease enter your name:\n')
    print("\nHello " + user_name + "!")
    return

def start_scene():
    print(“You’re a student at UC Berkeley, and you have just been assigned a new CS project.“)
    choices = [‘Feed the squirrel.’, ‘Kick the squirrel.’]
    list_choices(choices)
    choice = input(“What do you decide to do?”)
    
def party():
    print(“Instead of working you decide to go to a party!!”)
    choices = [‘It's a study party for a class more important than CS... (study party)’, ‘Turnt up!! (turn up)’]
    print(choices[0])

def user_death():
    print("You have died and failed. Goodbye.")
    return

def list_choices(choices):
    print(choices[0] + “\n” + choices[1])

def user_success():
    print("You have beat the game! Congratulations! Enjoy the rest of your day.")

main()
Jonathans-MacBook-Pro:introhack jonathan$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   main.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.DS_Store

no changes added to commit (use "git add" and/or "git commit -a")
Jonathans-MacBook-Pro:introhack jonathan$ python3 main.py
  File "main.py", line 7
    print(“You’re a student at UC Berkeley, and you have just been assigned a new CS project.“)
                ^
SyntaxError: invalid character in identifier
Jonathans-MacBook-Pro:introhack jonathan$ python3 main.py
  File "main.py", line 7
    print(“You are a student at UC Berkeley, and you have just been assigned a new CS project.“)
             ^
SyntaxError: invalid character in identifier
Jonathans-MacBook-Pro:introhack jonathan$ vim main.py

def main():
    user_name = input('\nHello, and welcome to the game. Prepare for an adventure!\nLoading game...\nPlease enter your name:\n')
    user_name = user_name[1:] + user_name[0] + 'ay'
    print("\nHello " + user_name + "!")
    start_scene()
    return

def start_scene():
    print("You are a student at UC Berkeley, and you have just been assigned a new CS project.")
    choices = ["Start now.", "Start later."]
    choice = user_decide(choices)
    if choice == 0:
        squirrel()
    if choice == 1:
        party()

def squirrel():
    print("Great! You are on your way to Soda when sUdDenly a wild squiRrel appears!!!")
    choices = ['Feed squirrel', 'Kick squirrel.']
    choice = user_decide(choices)
    if choice == 0:
        feed_squirrel()
    if choice == 1:
        kick_squirrel()

def party():
    print("Instead of working you decide to go to a party!!")
    choices = ["It's a study party for a class more important than CS...", 'Turnt up!!']
    choice = user_decide(choices)
    if choice == 0:
        study_party()
    if choice == 1:
        turn_up()

def feed_squirrel():
    print("That squirrel bites you!!")
    choices = ["Bite it back!", "Head over to the Tang Center because you forgot to waive SHIP and your health is your number one priority."]
"main.py" 131L, 3754C written
