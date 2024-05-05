import { Box, Button, Typography } from "@mui/material";
import CollapsibleTab from "../shared/collapsibleTab";

function getAllFeatures(features) {
  let allFeatures = [];

  Object.keys(features).forEach(key => {
    Object.keys(features[key]).forEach(secondaryKey => {
      allFeatures = allFeatures.concat(features[key][secondaryKey]);
    });
  });

  return allFeatures;
}

export default function FeaturesPanel({ features }) {
  //   // Add all
  //   let allFeatures = getAllFeatures(features);
  //   let pinned = ["Magical Tinkering", "Spellcasting", "Infuse Item"];

  //   let pinnedFeatures = allFeatures
  //     .filter(feature => pinned.includes(feature.name))
  //     .map(feature =>
  //       <CollapsibleTab
  //         key={feature.name}
  //         name={feature.name}
  //         text={feature.text}
  //       />
  //     );

  let pinnedFeatures = [];

  return (
    <Box
      sx={{ border: "1px solid black", height: "100%", borderRadius: "10px" }}
    >
      Features
      {pinnedFeatures}
    </Box>
  );
}
