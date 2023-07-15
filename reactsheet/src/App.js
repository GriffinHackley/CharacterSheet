import Sheet from "./Sheet";
import CharSelect from "./CharSelect";
import { Routes, Route } from "react-router-dom";
import Plan from "./Plan";
import Create from "./Create";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<CharSelect />} />
      <Route path="/character/:id" element={<Sheet />} />
      <Route path="/character/:id/plan" element={<Plan />} />
      <Route path="/create" element={<Create />} />
    </Routes>
  );
}
