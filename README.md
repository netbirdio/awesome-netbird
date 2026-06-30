# Awesome NetBird

> A curated list of community projects and content for [NetBird](https://netbird.io) — the open-source, WireGuard-based zero-configuration mesh VPN.

This repository is the source of truth for the community directory on [netbird.io](https://netbird.io). Each entry lives in its own file under [`data/`](data/); the site reads from this repository, so adding an entry here adds it to the website. To submit one, see [CONTRIBUTING.md](CONTRIBUTING.md).

**10 projects** · **12 pieces of content**

## Contents

- [Projects](#projects) (10)
- [Content](#content) (12)

## Projects

**Legend:** `🟢 Official` built and maintained by the NetBird team · `⭐ Endorsed` a community project the NetBird team vouches for.

### Apps

_Run or deploy NetBird somewhere — images, clients, and devices._

- **[Home Assistant Add-on](https://github.com/netbirdio/addon-netbird)** `🟢 Official` — The official NetBird add-on for Home Assistant, connecting your smart home to your private network in a few clicks with no port forwarding. _by NetBird_

### Extensions

_Plug NetBird into another tool or platform._

- **[NetBird for OpenWrt](https://github.com/netbirdio/openwrt-netbird)** `🟢 Official` — The official OpenWrt package that runs NetBird on your router for secure mesh networking, with setup-key login and init scripts. _by NetBird_
- **[NetBird for pfSense](https://github.com/netbirdio/pfsense-netbird)** `🟢 Official` — The official pfSense package that adds NetBird to your firewall, managed from the pfSense web UI under the VPN menu. _by NetBird_
- **[NetBird for Unraid](https://github.com/netbirdio/netbird-unraid)** `🟢 Official` — The official NetBird plugin for Unraid, making your Unraid server a native peer on your NetBird network with no extra container or hop. _by NetBird_
- **[NetworkManager Plugin](https://github.com/netbirdio/network-manager-vpn-plugin)** `🟢 Official` — The official NetworkManager VPN plugin that lets you manage NetBird connections from your Linux desktop's standard VPN controls. _by NetBird_

### Interfaces

_View or drive NetBird — CLIs, dashboards, and exporters._

- **[netbird-management-cli](https://github.com/TechHutTV/netbird-management-cli)** `⭐ Endorsed` — An unofficial Go CLI to manage NetBird peers, groups, policies, and DNS from the terminal via the REST API. _by TechHutTV_

### Tools

_Automate or manage NetBird via code — libraries and infrastructure as code._

- **[Ansible Collection](https://github.com/netbirdio/ansible-netbird)** `🟢 Official` — The official Ansible collection for managing self-hosted NetBird infrastructure (users, peers, policies, routes, and DNS) via the REST API. _by NetBird_
- **[Crossplane Provider](https://github.com/netbirdio/netbird-crossplane-provider)** `🟢 Official` — The official Crossplane provider for managing NetBird resources from Kubernetes-native infrastructure pipelines. _by NetBird_
- **[Kubernetes Operator](https://github.com/netbirdio/kubernetes-operator)** `🟢 Official` — The official operator that provisions NetBird access for Kubernetes workloads declaratively, managing peers, routes, and groups as custom resources. _by NetBird_
- **[Terraform Provider](https://github.com/netbirdio/terraform-provider-netbird)** `🟢 Official` — The official Terraform provider for managing your NetBird account and its resources as infrastructure as code. _by NetBird_

## Content

_Community videos, articles, and posts about NetBird. ⭐ marks featured items._

### Videos

- **[NetBird Setup Guide (New & Simplified)](https://www.youtube.com/watch?v=1BQdldvOC7w)** ⭐ — _by Christian Lempa_
- **[NetBird VPN & Pi-Hole DNS Setup](https://www.youtube.com/watch?v=4tuK8A4_gV4)** ⭐ — _by Jason's Lab_
- **[NAS als Mini-Server: n8n & KI-Agenten zu Hause laufen lassen (Terramaster F4-425 Pro)](https://www.youtube.com/watch?v=C26MtK-GVtc)** — _by Philip Thomas_
- **[NetBird Reverse Proxy: Better than Cloudflare Tunnels?](https://www.youtube.com/watch?v=-yfE3Lb3hTI)** — _by ServersatHome_
- **[NetBird vs Tailscale: The One I’d Trust With My #homelab](https://www.youtube.com/watch?v=jnGsStleHd0)** — _by 45HomeLab_
- **[NetBird: The Easy-to-Use Open-Source WireGuard Overlay VPN You Can Self-Host](https://www.youtube.com/watch?v=Kwrff6h0rEw)** — _by Lawrence Systems_
- **[REAL Self-Hosted Remote Access for YOUR Home Server](https://www.youtube.com/watch?v=z0HPuNFkmt4)** — _by TechHut_
- **[The EASIEST Unattended Remote Desktop for GNOME/Wayland.](https://www.youtube.com/watch?v=7ikzAnjk6YM)** — _by Cameron Knauff_
- **[This Underrated Tool Replaced 3 Homelab Services (and it's open source!)](https://www.youtube.com/watch?v=3wJ0IQ3rHjA)** — _by DevOps Toolbox_

### Articles

- **[Deploying the NetBird Reverse Proxy on Kubernetes](https://konst.fish/blog/netbird-reverse-proxy-on-kubernetes)** ⭐ — _by David Fischer_
- **[I was exposing my home server every time I opened a router port — NetBird fixed it](https://www.makeuseof.com/was-exposing-home-server-every-time-opened-router-port-netbird-fixed/)** — _by MakeUseOf_
- **[NetBird VPN homelab: ho sostituito Tailscale in 12 minuti e 3 subnet](https://homelabz.cc/blog/netbird-vpn-homelab-tailscale-migrazione)** — _by Antonio Distefano_

## Contributing

Found a NetBird project or piece of content that belongs here? Open a pull request adding one file under [`data/`](data/). See [CONTRIBUTING.md](CONTRIBUTING.md) for the format and review criteria.

