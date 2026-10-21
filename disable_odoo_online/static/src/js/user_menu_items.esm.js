import {registry} from "@web/core/registry";
// Needed so that this is run after adding the menu entries
import {user_menu_items} from "@web/webclient/user_menu/user_menu_items"; // eslint-disable-line no-unused-vars

const userMenuItems = registry.category("user_menuitems");

userMenuItems.remove("support");

// "My Subscription" comes from the optional mysubscription module, which we
// don't depend on: remove its entry whether it is registered before or after
// this file is loaded.
const MYSUBSCRIPTION_ITEM = "mysubscription_user_menu";
if (userMenuItems.contains(MYSUBSCRIPTION_ITEM)) {
    userMenuItems.remove(MYSUBSCRIPTION_ITEM);
}
userMenuItems.addEventListener("UPDATE", ({detail}) => {
    if (detail.operation === "add" && detail.key === MYSUBSCRIPTION_ITEM) {
        userMenuItems.remove(MYSUBSCRIPTION_ITEM);
    }
});
