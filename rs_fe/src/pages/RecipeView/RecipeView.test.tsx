import React from 'react';
import ReactDOM from 'react-dom';
import RecipeView from './RecipeView';

it('It should mount', () => {
  const div = document.createElement('div');
  ReactDOM.render(<RecipeView />, div);
  ReactDOM.unmountComponentAtNode(div);
});