#!/usr/bin/env python3
# Fabfile defining functions to pack, deploy, and clean the
# current directory to a remote server.
from fabric import task


@task
def pack(c):
    """Create a tar gzipped archive of the current directory."""
    c.run("touch mywebapp.tar.gz")
    c.run("tar --exclude='*.tar.gz' -cvzf mywebapp.tar.gz .")


@task
def deploy(c):
    """Upload the archive to the remote server in the /tmp/ directory."""
    c.user = "ubuntu"
    c.put("mywebapp.tar.gz", "/tmp")
    c.run("mkdir /tmp/mywebapp")
    c.run("tar -C /tmp/mywebapp -xzvf /tmp/mywebapp.tar.gz")


@task
def clean(c):
    """Deletes mywebapp.tar.gz on the local machine."""
    c.run("rm mywebapp.tar.gz")
