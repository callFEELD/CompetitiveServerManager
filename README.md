# CompetitiveServerManager

A TF2 config file to easily manage comp servers (rcon required)

## How to install

- place the `csm.cfg` into your `tf/cfg` folder
- add the line `exec csm` to your tf2 `autoexec.cfg` or just simply run `exec csm` in the tf2 console

## How to use

Just type `csm` into your tf2 console:

```
] csm

> csm_enable | Group
> csm_disable | Group
> csm_reload | Group
> csm_etf2l | Group
> csm_ugc | Group
> csm_rgl | Group
```

This is the output. A list with available commands you can start browsing and using.

I.e. you can change the servers config to the `etf2l 6s 5cp` config like so:

```
] csm_etf2l_6s_5cp
> executing command ...
```

Just make sure you already provided the `rcon password`.

```
] rcon_password YOUR_PASSWORD
```

Otherwise you will get this error:

```
] csm_etf2l_6s_5cp
> executing command ...
*SPEC* cF :  [CSM] executed csm_etf2l_6s_5cp
Bad RCON password
```
