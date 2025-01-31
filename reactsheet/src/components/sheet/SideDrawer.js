import { Link } from "react-router-dom";
import React, { useState } from "react";
import defaultLayout from "../../layouts/defaultLayout";
import { storeLayout } from "../../utils/localState.js";

import {
  Box,
  Button,
  Divider,
  Drawer,
  List,
  ListItem,
  ListItemText,
  ListItemButton,
  Switch
} from "@mui/material";

export default function SideDrawer({ id, character, editMode, setEditMode }) {
  const [drawerOpen, setDrawerOpen] = useState(false);
  const toggleDrawer = newOpen => () => {
    setDrawerOpen(newOpen);
  };

  const DrawerList = (
    <Box sx={{ width: 250 }} role="presentation" onClick={toggleDrawer(false)}>
      <List>
        <ListItem
          component={Link}
          to={`/character/${id}/features/`}
          state={{ featuresInfo: character.features }}
        >
          <ListItemText>Features</ListItemText>
        </ListItem>
        <ListItem
          component={Link}
          to={`/character/${id}/equipment/`}
          state={{ featuresInfo: character.equipment }}
        >
          <ListItemText>Equipment</ListItemText>
        </ListItem>
        <ListItem
          component={Link}
          to={`/character/${id}/spells/`}
          state={{ spellInfo: character.spells, config: character.config }}
        >
          <ListItemText>Spells</ListItemText>
        </ListItem>
        <ListItem
          component={Link}
          to={`/character/${id}/flavor/`}
          state={{ flavorInfo: character.flavor }}
        >
          <ListItemText>Flavor</ListItemText>
        </ListItem>
        <ListItem
          component={Link}
          to={`/character/${id}/graph/`}
          state={{ graphInfo: character.graph, toggles: character.toggles }}
        >
          <ListItemText>Graph</ListItemText>
        </ListItem>
      </List>
      <Divider />
      <List>
        <ListItem>
          <Switch
            onChange={newValue => setEditMode(newValue.target.checked)}
            checked={editMode}
          />
          <ListItemText>Edit Mode</ListItemText>
        </ListItem>
        <ListItemButton
          onClick={() => {
            storeLayout(id, defaultLayout());
            setEditMode(false);
          }}
        >
          <ListItemText>Use Default Layout</ListItemText>
        </ListItemButton>
        <ListItem to={`/character/${id}/plan/`} component={Link}>
          <ListItemText>Plan</ListItemText>
        </ListItem>
      </List>
    </Box>
  );

  return (
    <div>
      <Button onClick={toggleDrawer(true)}>Open drawer</Button>
      <Drawer open={drawerOpen} onClose={toggleDrawer(false)}>
        {DrawerList}
      </Drawer>
    </div>
  );
}
