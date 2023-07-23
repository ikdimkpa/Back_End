# edit ssh config file for privatekey and passwd authentication
exec {'Turn off passwd auth':
  path    => '/usr/bin:/bin',
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config'
}

exec {'Declare identity file':
  path    => '/usr/bin:/bin',
  command => 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
}
