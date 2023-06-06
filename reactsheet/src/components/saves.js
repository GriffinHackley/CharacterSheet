export default function Saves({savesInfo}){
    let saves = []

    savesInfo.forEach(element => {
        saves.push(
            <li class="tooltip shiftedRight" data-tooltip={ element.source }>
                <span class="saveName">{ element.name }</span>
                <div class="value">
                    { element.value }
                </div>
            </li>
        )
    });

    return (
        <div class="saves list-section">
          <ul>
            {saves}
          </ul>
          <div class="label">
            Saving Throws
          </div>
        </div>
    )
}