require 'gema'

describe Gema::HumanPlayer do
before :each do
@hp = Gema::HumanPlayer.new("X")
end

it "Debe existir un metodo move" do
@hp.respond_to?("move").should == true
end

it "Debe existir un metodo finish" do
@hp.respond_to?("finish").should == true
end
end
