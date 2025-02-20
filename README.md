# **Projet de Compression Audio IRM**  

## **Présentation**  
Le projet **IRM Audio Compression** est un outil personnalisé d'encodage et de lecture audio basé sur un nouveau format `.irm`. Ce format utilise des algorithmes de compression, notamment **LZW (Lempel-Ziv-Welch)**, afin de **réduire la taille des fichiers audio** tout en maintenant leur qualité.  

Le projet inclut des fonctionnalités permettant de convertir des fichiers audio standards (**.wma, .wav**) vers le format **.irm**, et inversement, ainsi qu’un lecteur pour la lecture des fichiers `.irm`.  

---

## **Structure du projet**  

### **Fichiers audio d'exemple**  
- **Free_Test_Data_1MB_WAV.wav** : Exemple de fichier audio WAV.  
- **Free_Test_Data_1MB_WMA.wma** : Exemple de fichier audio WMA.  
- **Free_Test_Data_1MB_WAV.irm** : Fichier compressé `.irm` généré à partir du fichier WAV.  
- **Free_Test_Data_2MB_WMA.wma** : Fichier WMA supplémentaire pour les tests.  

### **Scripts**  
- **main.py** : Contient la logique principale d'encodage et de décodage des fichiers `.irm`.  
- **main.ipynb** : Un Notebook Jupyter permettant de tester et démontrer les fonctionnalités d’encodage et de décodage de manière interactive.  

### **Dépendances**  
- **requirements.txt** : Liste des bibliothèques Python nécessaires pour exécuter le projet.  

---

## **Installation**  
1. **Cloner le dépôt** :  
   ```bash
   git clone https://github.com/votre-utilisateur/irm-audio-compression.git
   cd irm-audio-compression
   ```
2. **Installer les dépendances** :  
   ```bash
   pip install -r requirements.txt
   ```

---

## **Utilisation**  

### **Exécuter le script principal**  
Pour encoder ou décoder des fichiers audio, exécutez le script :  
```bash
python main.py
```

### **Convertir un fichier audio en format IRM**  
Chargez un fichier **WMA ou WAV** et utilisez les fonctions fournies pour le compresser au format `.irm`.  

### **Lire un fichier IRM**  
Le script inclut des fonctionnalités permettant de **décoder les fichiers `.irm`** afin qu'ils puissent être lus ou analysés.  

---

## **Principales fonctionnalités**  

### **Encodage**  
✔️ **Compression des fichiers audio** avec l’algorithme **LZW** et stockage au format `.irm`.  

### **Décodage et Lecture**  
✔️ **Décompression des fichiers `.irm`** pour retrouver un format audio lisible.  

---

## **Compétences et Apprentissage**  
🎵 **Compression audio** : Application pratique de l'algorithme LZW.  
🐍 **Programmation Python** : Encapsulation des fonctions d'encodage et de décodage.  
🔊 **Bibliothèques audio** : Utilisation de **pydub, pygame et sounddevice** pour la gestion du son.  
📜 **Jupyter Notebooks** : Documentation et démonstration des fonctionnalités via `main.ipynb`.  

