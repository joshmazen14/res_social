import React, { FC } from 'react';
import styles from './Auth.module.scss';

interface AuthProps {}

const Auth: FC<AuthProps> = () => (
  <div className={styles.Auth}>
    Auth Component
  </div>
);

export default Auth;
