import '../css/Attributes.css';

export default function Attributes({attributesInfo}){
    let attributes = []

    attributesInfo.forEach(element => {
        attributes.push(
            <li class="tooltip shiftedRight" data-tooltip={ element.source }>
                <div class="mod">
                  <div class="abilityName">{ element.name }</div>
                  <div class="abilityMod">{ element.mod }</div>
                </div>
                <div class="abilityScore">
                  <div class="score">{ element.score }</div>
                </div>
            </li>
        )
    });

    return (
        <section class="attributes">
        <div class="scores">
          <ul>
            {attributes}
          </ul>
        </div>
      </section>
    )
}