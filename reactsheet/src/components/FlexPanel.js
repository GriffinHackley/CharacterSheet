import FeaturesTab from "./FeaturesTab";
import FlexHeader from "./FlexHeader";

export default function FlexPanel({panelInfo}){
    return (
        <section class="flexPanel">
            <FlexHeader></FlexHeader>
            <FeaturesTab featuresInfo={panelInfo}></FeaturesTab>
        </section>
    )
}