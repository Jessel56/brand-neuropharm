// Extracted from customthem.txt block 29 (check_membership.py) - Preview: import React from "react"; export default function AccessTemplate({ tier }) {   

import React from "react";
export default function AccessTemplate({ tier }) {
  return (
    <div>
      <h2>Access Restricted</h2>
      <p>Your current tier: {tier}</p>
    </div>
  );
}