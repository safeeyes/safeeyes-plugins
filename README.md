# Safe Eyes Third-party Plugins

This repository is a place for third-party developers to share their plugins written for Safe Eyes. You have the full freedom to distribute and share using any mediums. However, I have created this repository as a place which is easily accessible to the developers via the link shared in the Safe Eyes official website.

## Developers

I welcome Safe Eyes users to write their own custom plugins and share them here by sending a pull request. However, I do apply some restrictions to the plugins if you want them to be added to this repository:

1. The plugin must be shared under GPL v3 license.

    WHY? I highly believe and support FOSS and among the licenses, I know so far, GPL v3 ensures that the users have full freedom on the code. Further, if anyone copies your code, they must release their entire product under GPL v3 which is good for the FOSS community.

    Please add the GPL v3 license header in `plugin.py` file.

2. The plugin must have an icon.

3. The plugin should be highly cohesive. If you have several ideas, develop them as individual plugins.

## Users

### Installation

1. Clone this repository

```sh
git clone https://github.com/safeeyes/safeeyes-plugins.git
```

2. Create a new folder `~/.config/safeeyes/plugins` if it does not exist already.

```sh
mkdir ~/.config/safeeyes/plugins
```

3. Copy the desired plugin folder to the above directory.

```sh
cp -r ./safeeyes-plugins/weather ~/.config/safeeyes/plugins/weather
```

4. Restart Safe Eyes

5. Check the Plugins tab in Safe Eyes settings dialog for the newly installed plugin.

**Notice:**
I try my best to manually analyze the plugins submitted by other developers to ensure that they don't misuse the plugin. I hope other users using Safe Eyes also will keep an eye on this. Anyhow as everything is under GPL v3 license, the plugins are distributed WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

