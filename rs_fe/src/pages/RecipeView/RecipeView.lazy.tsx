import React, { lazy, Suspense } from 'react';

const LazyRecipeView = lazy(() => import('./RecipeView'));

const RecipeView = (props: JSX.IntrinsicAttributes & { children?: React.ReactNode; }) => (
  <Suspense fallback={null}>
    <LazyRecipeView {...props} />
  </Suspense>
);

export default RecipeView;
