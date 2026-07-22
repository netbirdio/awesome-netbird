# Awesome NetBird

> A curated list of community projects and content for [NetBird](https://netbird.io) — the open-source, WireGuard-based zero-configuration mesh VPN.

This repository is the source of truth for the community directory on [netbird.io](https://netbird.io). Each entry lives in its own file under [`data/`](data/); the site reads from this repository, so adding an entry here adds it to the website. To submit one, see [CONTRIBUTING.md](CONTRIBUTING.md).

**36 projects** · **18 pieces of content**

## Contents

- [Projects](#projects) (36)
- [Content](#content) (18)

## Projects

**Legend:** `🟢 Official` built and maintained by the NetBird team · `⭐ Endorsed` a community project the NetBird team vouches for.

### Apps

_Run or deploy NetBird somewhere — images, clients, and devices._

- **[Home Assistant Add-on](https://github.com/netbirdio/addon-netbird)** `🟢 Official` — The official NetBird add-on for Home Assistant, connecting your smart home to your private network in a few clicks with no port forwarding. _by NetBird_
- **[NetBird Helm Chart](https://github.com/netbirdio/helms/tree/main/charts/netbird)** `🟢 Official` — Official Helm chart for deploying NetBird's self-hosted control plane (management, signal, relay, and dashboard) into a Kubernetes cluster, with ingress, persistence, and monitoring support. _by NetBird_
- **[NetBird for NixOS](https://github.com/NixOS/nixpkgs/tree/master/pkgs/by-name/ne/netbird)** `⭐ Endorsed` — NetBird client package and services.netbird module in nixpkgs for declaratively installing and configuring the NetBird client on NixOS. _by nixpkgs maintainers_
- **[NetBird Proxmox LXC](https://community-scripts.org/scripts/add-netbird-lxc?id=add-netbird-lxc)** `⭐ Endorsed` — Community helper script that creates a Proxmox VE LXC container running the NetBird client, set up as a routing peer to bridge your Proxmox network into your NetBird network. _by Community Scripts_
- **[NetBird Snap](https://github.com/ubuntu-robotics/netbird_snap)** `⭐ Endorsed` — Snap package of the NetBird client for Linux, letting you install and run NetBird on Ubuntu and other snapd-compatible distributions via the Snap Store. _by Ubuntu Robotics_
- **[docker-netbird](https://github.com/11notes/docker-netbird)** — A rootless, distroless Docker image that packages the NetBird management server, dashboard, and signal server into one lightweight container. _by 11notes_
- **[JetBird](https://codeberg.org/bg443/JetBird)** — An unofficial, privacy-focused native Android client for NetBird, adding split tunneling, per-app exclusion, and Rosenpass support. Available on F-Droid. _by bg443_
- **[mavlink-anywhere](https://github.com/alireza787b/mavlink-anywhere)** — A companion-computer routing dashboard for drone MAVLink telemetry that uses NetBird for secure remote access to ground stations and operators. _by alireza787b_
- **[nanoNetBird](https://github.com/bc547/nanoNetBird)** — Brings the NetBird client to nanoKVM out-of-band management devices, with a single-command install that auto-updates. _by bc547_
- **[NetBird Dockhand Templates](https://github.com/shaban00/netbird-dockhand)** — Dockhand stack templates for one-click deployment of a self-hosted NetBird control plane: combined server (management, signal, relay, STUN, embedded Dex IdP), dashboard, Postgres, NetBird reverse proxy, CrowdSec, and Caddy with TLS passthrough. Includes a client stack template. _by shaban00_
- **[NetBird on Arch (AUR)](https://aur.archlinux.org/packages/netbird)** — AUR package that builds and installs the NetBird client from source on Arch Linux, with a prebuilt netbird-bin variant also available. _by tarball_

### Extensions

_Plug NetBird into another tool or platform._

- **[NetBird for pfSense](https://github.com/netbirdio/pfsense-netbird)** `🟢 Official` — The official pfSense package that adds NetBird to your firewall, managed from the pfSense web UI under the VPN menu. _by NetBird_
- **[NetBird for Unraid](https://github.com/netbirdio/netbird-unraid)** `🟢 Official` — The official NetBird plugin for Unraid, making your Unraid server a native peer on your NetBird network with no extra container or hop. _by NetBird_
- **[NetworkManager Plugin](https://github.com/netbirdio/network-manager-vpn-plugin)** `🟢 Official` — The official NetworkManager VPN plugin that lets you manage NetBird connections from your Linux desktop's standard VPN controls. _by NetBird_
- **[caddy-netbird](https://github.com/lixmal/caddy-netbird)** `⭐ Endorsed` — A Caddy plugin that embeds a NetBird client, letting the reverse proxy route HTTP and raw TCP/UDP traffic to upstreams through a NetBird network instead of the public internet. _by lixmal_
- **[NetBird API Exporter](https://github.com/matanbaruch/netbird-api-exporter)** `⭐ Endorsed` — Prometheus exporter that collects metrics from the NetBird API (peers, groups, users, networks, and DNS) and exposes them for monitoring, with a prebuilt Grafana dashboard. _by Matan Baruch_
- **[NetBird for OpenWrt](https://github.com/netbirdio/openwrt-netbird)** `⭐ Endorsed` — The official OpenWrt package that runs NetBird on your router for secure mesh networking, with setup-key login and init scripts. _by NetBird_
- **[netbird-connect](https://github.com/Alemiz112/netbird-connect)** `⭐ Endorsed` — A GitHub Action that joins your CI/CD runners to a NetBird network so workflows can reach private resources securely. _by Alemiz112_
- **[luci-app-netbird](https://github.com/looong-cat/luci-app-netbird)** — A LuCI web UI for managing the NetBird client on OpenWrt / ImmortalWrt routers, with one-click firewall zone and LAN-to-mesh forwarding setup. _by looong-cat_
- **[NetBird Connect Runner](https://github.com/shaban00/netbird-connect)** — A GitHub Action that joins a workflow runner to your NetBird network as an ephemeral peer, so CI/CD jobs can reach private resources like internal services, databases, and jump hosts over WireGuard. _by shaban00_
- **[NetBird Expose Runner](https://github.com/shaban00/netbird-expose)** — A GitHub Action that builds a project's Docker service on the workflow runner and exposes it through the NetBird reverse proxy with automatic TLS and optional auth, holds it live for a configurable duration, then tears down the ephemeral peer. _by shaban00_
- **[NetBird for Talos Linux](https://github.com/siderolabs/extensions/tree/main/network/netbird)** — Talos Linux system extension that runs the NetBird client on Talos nodes, giving machines on your NetBird network secure access to your Talos Kubernetes nodes. _by Sidero Labs_
- **[NetBird HomeAssistant integration](https://github.com/jose1711/netbird-ha/)** — Home Assistant integration that monitors your NetBird network: peers, legacy routes and network resources (with their routers). _by jose1711_
- **[NetBird VPN for Decky Loader](https://github.com/MentallyOverwhelmed/decky-netbird)** — A Decky Loader plugin to manage NetBird VPN directly from the Steam Deck Quick Access Menu. Authenticate via SSO/QR, manage peers, network resources, port exposure, forwarding rules, and profiles. All from the gaming-mode UI. _by MentallyOverwhelmed_
- **[netbird-traefik](https://github.com/yblis/netbird-traefik)** — Run NetBird behind a Traefik reverse proxy using Traefik labels, without changing your existing stack. _by yblis_
- **[NetDesk](https://github.com/yblis/NetDesk)** — A Chrome extension that adds one-click RustDesk remote access (desktop, terminal, file transfer) right inside the NetBird dashboard. _by yblis_

### Interfaces

_View or drive NetBird — CLIs, dashboards, and exporters._

- **[netbird-exporter](https://github.com/gocloudio/netbird-exporter)** — A Prometheus exporter that surfaces NetBird peer connection status, latency, and traffic metrics for your dashboards. _by gocloudio_
- **[netbird-tui](https://github.com/n0pashkov/netbird-tui)** — A terminal UI for the local NetBird daemon that uses the daemon gRPC socket for keyboard-driven monitoring and management of peers, routes, DNS, and more. _by n0pashkov_

### Tools

_Automate or manage NetBird via code — libraries and infrastructure as code._

- **[Crossplane Provider](https://github.com/netbirdio/netbird-crossplane-provider)** `🟢 Official` — The official Crossplane provider for managing NetBird resources from Kubernetes-native infrastructure pipelines. _by NetBird_
- **[Kubernetes Operator](https://github.com/netbirdio/kubernetes-operator)** `🟢 Official` — The official operator that provisions NetBird access for Kubernetes workloads declaratively, managing peers, routes, and groups as custom resources. _by NetBird_
- **[Terraform Provider](https://github.com/netbirdio/terraform-provider-netbird)** `🟢 Official` — The official Terraform provider for managing your NetBird account and its resources as infrastructure as code. _by NetBird_
- **[Ansible Collection](https://github.com/netbirdio/ansible-netbird)** `⭐ Endorsed` — The official Ansible collection for managing self-hosted NetBird infrastructure (users, peers, policies, routes, and DNS) via the REST API. _by NetBird_
- **[ansible-netbird](https://github.com/dominion-solutions/ansible-netbird)** — An Ansible collection for deploying and managing NetBird servers and peers, with dynamic inventory for peer data. _by Dominion Solutions_
- **[netbird-delayed-auto-update-windows](https://github.com/NetHorror/netbird-delayed-auto-update-windows)** — A PowerShell script and scheduled task that delays NetBird Windows client updates by a set number of days to avoid rolling out bad releases. _by NetHorror_
- **[netbird-mullvad-bypass](https://github.com/d10n/netbird-mullvad-bypass)** — An nftables-based bypass that lets NetBird and Mullvad VPN coexist on Linux, with packages for Arch, Fedora/RHEL, and Debian/Ubuntu. _by d10n_
- **[netbird-python-client](https://github.com/drtinkerer/netbird-python-client)** — An unofficial Python client library for the NetBird API, covering 30+ resources for managing your network as code. _by drtinkerer_

## Content

_Community videos, articles, and posts about NetBird. ⭐ marks featured items._

### Videos

- **[NetBird Setup Guide (New & Simplified)](https://www.youtube.com/watch?v=1BQdldvOC7w)** ⭐ — _by Christian Lempa_
- **[NAS als Mini-Server: n8n & KI-Agenten zu Hause laufen lassen (Terramaster F4-425 Pro)](https://www.youtube.com/watch?v=C26MtK-GVtc)** — _by Philip Thomas_
- **[NetBird Reverse Proxy: Better than Cloudflare Tunnels?](https://www.youtube.com/watch?v=-yfE3Lb3hTI)** — _by ServersatHome_
- **[NetBird VPN & Pi-Hole DNS Setup](https://www.youtube.com/watch?v=4tuK8A4_gV4)** — _by Jason's Lab_
- **[Netbird VPN access for Kubernetes](https://www.youtube.com/watch?v=hygaBdCRj18)** — _by Engineering with Morris_
- **[NetBird vs Tailscale: The One I’d Trust With My #homelab](https://www.youtube.com/watch?v=jnGsStleHd0)** — _by 45HomeLab_
- **[NetBird: The Easy-to-Use Open-Source WireGuard Overlay VPN You Can Self-Host](https://www.youtube.com/watch?v=Kwrff6h0rEw)** — _by Lawrence Systems_
- **[REAL Self-Hosted Remote Access for YOUR Home Server](https://www.youtube.com/watch?v=z0HPuNFkmt4)** — _by TechHut_
- **[Schluss mit Port-Forwarding! NetBird macht Selfhosting sicherer](https://www.youtube.com/watch?v=B77znhDBw2w)** — _by Daniel Klozbücher / IT-ION GmbH_
- **[The EASIEST Unattended Remote Desktop for GNOME/Wayland.](https://www.youtube.com/watch?v=7ikzAnjk6YM)** — _by Cameron Knauff_
- **[This Underrated Tool Replaced 3 Homelab Services (and it's open source!)](https://www.youtube.com/watch?v=3wJ0IQ3rHjA)** — _by DevOps Toolbox_

### Articles

- **[Deploying the NetBird Reverse Proxy on Kubernetes](https://konst.fish/blog/netbird-reverse-proxy-on-kubernetes)** ⭐ — _by David Fischer_
- **[I migrated my entire home lab network stack to NetBird because it does the one thing Tailscale can't match](https://www.xda-developers.com/i-migrated-my-entire-home-lab-stack-to-netbird-because-it-does-one-thing-tailscale-cant-match/)** ⭐ — _by XDA Developers_
- **[5 Lightweight Tailscale Alternatives Worth Running on Your Own Hardware](https://techdigestor.com/5-lightweight-tailscale-alternatives-worth-running-on-your-own-hardware/)** — _by techdigestor_
- **[Best.VPN.Ever.](https://blog.serversatho.me/best-vpn-ever/)** — _by ServersatHome_
- **[I was exposing my home server every time I opened a router port — NetBird fixed it](https://www.makeuseof.com/was-exposing-home-server-every-time-opened-router-port-netbird-fixed/)** — _by MakeUseOf_
- **[NetBird VPN homelab: ho sostituito Tailscale in 12 minuti e 3 subnet](https://homelabz.cc/blog/netbird-vpn-homelab-tailscale-migrazione)** — _by Antonio Distefano_
- **[NetBird vs Tailscale: Why the Layer 4 Reverse Proxy is Forcing Home Labs to Migrate](https://blazetrends.com/netbird-vs-tailscale-why-the-layer-4-reverse-proxy-is-forcing-home-labs-to-migrate/)** — _by Blaze Trends_

## Contributing

Found a NetBird project or piece of content that belongs here? Open a pull request adding one file under [`data/`](data/). See [CONTRIBUTING.md](CONTRIBUTING.md) for the format and review criteria.

