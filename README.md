# Awesome NetBird

> A curated list of community projects, tools, and integrations for [NetBird](https://netbird.io) — the open-source, WireGuard-based zero-configuration mesh VPN.

This list is the source of truth for the community projects directory on [netbird.io](https://netbird.io). Each entry lives in its own file under [`data/projects/`](data/projects/); the site reads from this repository, so adding a project here adds it to the website. To submit one, see [CONTRIBUTING.md](CONTRIBUTING.md).

**10 projects** · 🟢 9 official · ⭐ 1 endorsed · 0 community

## Contents

- [Apps](#apps) (1)
- [Extensions](#extensions) (4)
- [Interfaces](#interfaces) (1)
- [Tools](#tools) (4)

**Legend:** `🟢 Official` built and maintained by the NetBird team · `⭐ Endorsed` a community project the NetBird team vouches for.

## Apps

_Run or deploy NetBird somewhere — images, clients, and devices._

- **[Home Assistant Add-on](https://github.com/netbirdio/addon-netbird)** `🟢 Official` — The official NetBird add-on for Home Assistant, connecting your smart home to your private network in a few clicks with no port forwarding. _by NetBird_

## Extensions

_Plug NetBird into another tool or platform._

- **[NetBird for OpenWrt](https://github.com/netbirdio/openwrt-netbird)** `🟢 Official` — The official OpenWrt package that runs NetBird on your router for secure mesh networking, with setup-key login and init scripts. _by NetBird_
- **[NetBird for pfSense](https://github.com/netbirdio/pfsense-netbird)** `🟢 Official` — The official pfSense package that adds NetBird to your firewall, managed from the pfSense web UI under the VPN menu. _by NetBird_
- **[NetBird for Unraid](https://github.com/netbirdio/netbird-unraid)** `🟢 Official` — The official NetBird plugin for Unraid, making your Unraid server a native peer on your NetBird network with no extra container or hop. _by NetBird_
- **[NetworkManager Plugin](https://github.com/netbirdio/network-manager-vpn-plugin)** `🟢 Official` — The official NetworkManager VPN plugin that lets you manage NetBird connections from your Linux desktop's standard VPN controls. _by NetBird_

## Interfaces

_View or drive NetBird — CLIs, dashboards, and exporters._

- **[netbird-management-cli](https://github.com/TechHutTV/netbird-management-cli)** `⭐ Endorsed` — An unofficial Go CLI to manage NetBird peers, groups, policies, and DNS from the terminal via the REST API. _by TechHutTV_

## Tools

_Automate or manage NetBird via code — libraries and infrastructure as code._

- **[Ansible Collection](https://github.com/netbirdio/ansible-netbird)** `🟢 Official` — The official Ansible collection for managing self-hosted NetBird infrastructure (users, peers, policies, routes, and DNS) via the REST API. _by NetBird_
- **[Crossplane Provider](https://github.com/netbirdio/netbird-crossplane-provider)** `🟢 Official` — The official Crossplane provider for managing NetBird resources from Kubernetes-native infrastructure pipelines. _by NetBird_
- **[Kubernetes Operator](https://github.com/netbirdio/kubernetes-operator)** `🟢 Official` — The official operator that provisions NetBird access for Kubernetes workloads declaratively, managing peers, routes, and groups as custom resources. _by NetBird_
- **[Terraform Provider](https://github.com/netbirdio/terraform-provider-netbird)** `🟢 Official` — The official Terraform provider for managing your NetBird account and its resources as infrastructure as code. _by NetBird_

## Contributing

Found a NetBird project that belongs here? Open a pull request adding one file under [`data/projects/`](data/projects/). See [CONTRIBUTING.md](CONTRIBUTING.md) for the format and review criteria.

