# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.provision "shell", privilaged: false, inline <<-SHELL
    sudo apt-get update

    #Install pyenv prerequisites
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

    #Install pyenv
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
    exec "$SHELL"

    #Install python
    pyenv install 3.7.9
    pyenv global 3.7.9

    #Install poetry
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
  SHELL

  config.trigger.after :up do |trigger|
    trigger.name = "Launch App"
    trigger.info = "Running the TODO app setup script"
    trigger.run_remote = {privilaged: false, inline: "
      #Install dependencies and Launch
      cd /vagrant
      poetry install
      poetry run flask run --host=0.0.0.0
    "}
  end

  config.vm.network "forward_port", guest: 5000, host: 5000
end
