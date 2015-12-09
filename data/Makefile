download_data:
	wget http://openfmri.s3.amazonaws.com/tarballs/ds005_raw.tgz
	tar -xvzf ds005_raw.tgz

validate_data:
	wget http://openfmri.s3.amazonaws.com/tarballs/ds005_raw_checksums.txt
	python data.py

download_filtered_data:
	variable=Stop python ../data/filtered_data_sh_script.py
	variable=Stop bash ../data/dwn_filtered_data_script.sh
 	
	
