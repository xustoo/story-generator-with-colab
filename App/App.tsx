import React from 'react';
import { SafeAreaView } from 'react-native';
import StoryGenerator from './components/storyGenerator';

const App = () => {
  return (
    <SafeAreaView style={{ flex: 1 }}>
      <StoryGenerator />
    </SafeAreaView>
  );
};
export default App;
