const petalPath1 = `M0 0 C50 50 50 100 0 100 C-50 100 -50 50 0 0`;
const petalPath2 = `M0,0 C50,40 50,90 25,100 C10,105 5,95 0,85 C-5,95 -10,105 -25,100 C-50,90 -50,40 0,0`;
const petalPath3 = `M0,0 C50,40 50,65 45,80 C40,100 20,95 15,85 C10,105 -10,105 -15,85 C-20,95 -40,100 -45,80 C-50,65 -50,40 0,0`;
const petalPath4 = `M0,0 C55,30 65,110 27.5,85 C20,105 5,105 0,85 C-5,105 -20,105 -27.5,85 C-65,110 -55,30 0,0`;

const svg = html`
  <svg width="400" height="105">
    <path d="${petalPath1}" transform="translate(50, 0)" />
    <path d="${petalPath2}" transform="translate(150, 0)" />
    <path d="${petalPath3}" transform="translate(250, 0)" />
    <path d="${petalPath4}" transform="translate(350, 0)" />
  </svg>
`;

d3.select(svg)
  .selectAll('path')
  .attr('fill', 'none')
  .attr('stroke', '#643a6b')
  .attr('stroke-width', 2);

return svg;
