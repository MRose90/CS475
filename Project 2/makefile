proj1:
	g++ -DNUMT=1 proj0.cpp -o proj0 -lm -fopenmp
loop:
	echo "" > SC.csv; \
	echo "" > SF.csv; \
	echo "" > DC.csv; \
	echo "" > DF.csv; \
		for numt in 1 2 3 4 8 16; do \
			g++ -DNUMT=$$numt -DCOARSE=1  static.cpp -o static -lm -fopenmp ;\
			./static >>SC.csv ; \
			g++ -DNUMT=$$numt -DCOARSE=0  static.cpp -o static -lm -fopenmp ;\
			./static >>SF.csv ; \
			g++ -DNUMT=$$numt -DCOARSE=1  dynamic.cpp -o dynamic -lm -fopenmp ;\
			./dynamic >>DC.csv ; \
			g++ -DNUMT=$$numt -DCOARSE=0  dynamic.cpp -o dynamic -lm -fopenmp ;\
			./dynamic >>DF.csv ; \
		done; 
clean:
	rm -f *.o
