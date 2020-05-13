# Install Python and configure python
apt install -y python3
apt install -y python3-pip
pip3 install tweepy
pip3 install pandas

# Run The Web Crawler file to generate info.csv
python3 src/crawler/Crawl.py

# Install Java
apt install -y openjdk-11-jre-headless

# Install Maven
apt install -y maven

# Maven Builds
mvn clean
mvn test
mvn install
mvn site

# Move Crawler output Excel file to Sentimental Analysis workspace
mv src/crawler/info.csv src/sentimental_analysis

# Install Machine Learning libraries
pip3 install keras
pip3 install tensorflow

# Move to Machine Learning folder from Crawler folder
cd ..
cd sentimental_analysis

# Switch case to select Machine Learning Model
echo "Sentimental Analysis Use cases"

# Option Menu
echo "1) Random Forest"
echo "2) Decision Tree"
echo "3) Naive Bayes"
read -p "Enter your choice: " ch

# Switch case
case "$ch" in
1) python3 randomforest.py ;;

2) python3 decisiontree.py ;;

3) python3 naivebayes.py ;;

esac

# Visualization
apt-get install -y python3-matplotlib
cd ..
cd visualization
python3 matplotlib.py


