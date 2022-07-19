import React, { useState } from 'react';

export default function Checkbox({}) {
  const [state, setState] = useState(false);

  let handleCheckboxChange = (event: React.ChangeEvent<HTMLInputElement>) =>
    setState(event.target.checked);

  return (
    <div>
      <input type="text" />
    </div>
  );
}
