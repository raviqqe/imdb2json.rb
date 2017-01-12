require 'rake/clean'


IMDB_TAR = 'aclImdb_v1.tar.gz'
DATASET_FILE = "#{__dir__}/#{IMDB_TAR}"
DATASET_DIR = (ENV['dataset_dir'] or "#{__dir__}/aclImdb")


file DATASET_FILE do |t|
  mkdir_p File.dirname(t.name)
  sh "wget -O #{t.name} http://ai.stanford.edu/~amaas/data/sentiment/#{IMDB_TAR}"
end

directory DATASET_DIR => DATASET_FILE do |t|
  mkdir_p t.name
  sh "tar -C #{File.dirname t.name} -xf #{t.source}"
end

task :dataset => DATASET_DIR


CLEAN.include Dir.glob(['aclImdb', '*.gz'])
