import { CameraView } from 'expo-camera';
import { useEffect, useState } from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import ThemedButton from '../Components/ThemedButton';
import Title from '../Components/Title';
import LoadingBar from '../Components/LoadingBar';
import {usePipeline, FAILURE_MSG } from '../Hooks/usePipeline';
import useGyro from '../Hooks/useGyro'
import useCam from '../Hooks/useCam';


export default function RecordingScreen() {
  const [isRecording, setIsRecording] = useState(false)
  const { uploadProgress, uploadStatus, uploadVideo } = usePipeline()
  const cam = useCam(isRecording)
  const gyro = useGyro(isRecording)


  useEffect(() => {
    cam.requestPermissions();
  }, []);

  function toggleRecord() {
    if (isRecording) {
      console.log("Recording stopped")
      gyro.stopRecording()
      cam.stopRecording()
      setIsRecording(false)
    }
    else {
      console.log("Recording started")
      gyro.startRecording()
      cam.startRecording()
      setIsRecording(true)
    }
  }

  if (!cam.cameraPermission || !cam.microphonePermission) {
    return <View />;
  }

  if (!cam.cameraPermission.granted || !cam.microphonePermission.granted) {
    return (
      <View style={styles.container}>
        <Text style={{ textAlign: 'center' }}>We need your permission to show the camera</Text>
        <ThemedButton onPress={cam.requestPermissions} title="Grant Permission" />
      </View>
    );
  }

  return (
    <View style={{ ...styles.container, alignItems: cam.videoUri ? 'center' : 'left' }}>
      {cam.videoUri ? (
        <View>
          {uploadStatus == FAILURE_MSG && <ThemedButton
            title="Send Video"
            onPress={() => uploadVideo(cam.videoUri, gyro.data)}
          />}
          <Title text={uploadStatus} size={40} />
          <LoadingBar progress={uploadProgress} />
        </View>

      ) : (
        <View style={styles.camera}>
          <CameraView mode="video" style={styles.camera} ref={cam.cameraRef}>
            <View style={styles.buttonContainer}>
              <TouchableOpacity style={styles.button} onPress={toggleRecord}>
                <Text style={styles.recButton}>{isRecording ? "■" : "⬤"}</Text>
              </TouchableOpacity>
            </View>
          </CameraView>
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
  },
  recButton: {
    fontSize: 100,
    color: "#C41E3A"
  },

  camera: {
    flex: 1,
  },
  buttonContainer: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: 'transparent',
    margin: 5,
  },
  button: {
    flex: 1,
    alignSelf: 'flex-end',
    alignItems: 'center',
  },
  text: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
  },
});