FROM debian:11.6

ARG PACKAGE_LIST="\
    binutils \
    gcc \
    git \
    less \
    libc-dev \
    locales \
    make \
    man-db \
    manpages \
    manpages-dev \
    openssh-client \
    procps \
    sudo \
    vim \
"

# Install base packages
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends ${PACKAGE_LIST}

ARG USERNAME=elf
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create user
RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}

# Give user sudo permissions
RUN echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

# Locale generation
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen
