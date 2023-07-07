import Sheet from "./Sheet";
import CharSelect from "./CharSelect";
import { Routes, Route, Redirect } from "react-router-dom";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<CharSelect />} />
      <Route path="/character/:id" element={<Sheet />} />
    </Routes>
  );
}
