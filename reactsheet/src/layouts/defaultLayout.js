export default function defaultLayout(editMode, id, consumables) {
  console.log("Using default layout");
  let ret = [
    {
      i: "combat",
      x: 6,
      y: 0,
      w: 4,
      h: 6,
      minW: 3,
      minH: 6,
      static: !editMode
    },
    {
      i: "attacksandspellcasting",
      x: 6,
      y: 6,
      w: 4,
      h: 4,
      minW: 3,
      minH: 4,
      static: !editMode
    },
    { i: "proficiency", x: 10, y: 0, w: 2, h: 1, minW: 2, static: !editMode },
    { i: "passives", x: 10, y: 1, w: 2, h: 2, minH: 2, static: !editMode },
    {
      i: "toggles",
      x: 10,
      y: 5,
      w: 2,
      h: 5,
      minW: 2,
      minH: 3,
      static: !editMode
    },
    { i: "features", x: 0, y: 0, w: 6, h: 6, static: !editMode }
  ];

  let count = 0;
  for (let consumable in consumables) {
    ret.push({
      i: "consumable-" + consumable,
      x: 10 + count % 2,
      y: 3 + Math.floor(count / 2),
      w: 1,
      h: 2,
      minH: 2,
      static: !editMode
    });
    count++;
  }

  return ret;
}
