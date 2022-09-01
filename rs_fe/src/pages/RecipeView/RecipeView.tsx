import React, { FC } from 'react';
import styles from './RecipeView.module.scss';

interface RecipeViewProps {}

const RecipeView: FC<RecipeViewProps> = () => (
  <div className={styles.RecipeView}>
    RecipeView Component
  </div>
);

export default RecipeView;
