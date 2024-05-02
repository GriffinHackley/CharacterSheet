import Sheet from "./components/pages/Sheet";
import CharSelect from "./components/pages/CharSelect";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Plan from "./components/pages/Plan";
import Create from "./components/pages/Create";
import FeaturesTab from "./components/pages/Features";
import EquipmentTab from "./components/pages/Equipment";
import SpellTab from "./components/pages/Spells";
import FlavorTab from "./components/pages/Flavor";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<CharSelect />} />
        <Route path="/character/:id" element={<Sheet />} />
        <Route path="/character/:id/features" element={<FeaturesTab />} />
        <Route path="/character/:id/equipment" element={<EquipmentTab />} />
        <Route path="/character/:id/spells" element={<SpellTab />} />
        <Route path="/character/:id/flavor" element={<FlavorTab />} />
        <Route path="/character/:id/plan" element={<Plan />} />
        <Route path="/create" element={<Create />} />
      </Routes>
    </Router>
  );
}
