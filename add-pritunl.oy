---
- name: install pritunl client
  hosts: all
  become: yes
  tasks:
    - name: Create repository file
      copy:
        content: "deb http://repo.pritunl.com/stable/apt {{ ansible_distribution_release }} main"
        dest: "/etc/apt/sources.list.d/pritunl.list"

    - name: installing gnupg key
      apt:
        name: gnupg
        state: present
    - name: Manually importing gnupg key
      apt_key:
        keyserver: "hkp://keyserver.ubuntu.com"
        id: 7568D9BB55FF9E5287D586017AE645C0CF8E292A
    - name: exporting gpg key
      shell:
        cmd: "gpg --armor --export 7568D9BB55FF9E5287D586017AE645C0CF8E292A > /etc/apt/trusted.gpg.d/pritunl.asc"
    - name: Clear apt cache
      apt:
        autoclean: yes
        autoremove: yes
    - name: Update package cache
      shell:
        cmd: apt-get update
    - name: install pritunl client
      apt:
        name: pritunl-client-electron
        state: latest
    - name: Start Pritunl Client service
      service:
        name: pritunl-client
        state: started
        enabled: yes
