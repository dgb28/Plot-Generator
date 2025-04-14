FROM r-base

RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev \
    libx11-dev \
    pandoc \
    && rm -rf /var/lib/apt/lists/*
 \
    # Install dependencies
RUN R -e "install.packages(c('lattice', 'rgl', 'fs', 'htmlwidgets'), repos='http://cran.rstudio.com')"

# Set working directory
WORKDIR /code

# Copy your R script
COPY snippet.R .

# Run the script by default
CMD ["Rscript", "/code/snippet.R"]