#include <iostream>
#include <TCanvas.h>
#include <TH1.h>
#include <TH2.h>
#include <TH3.h>
#include <TFile.h>
#include <TTree.h>



void Dalitz_Analyse(){
  //File Oeffnen
  auto f1 = TFile::Open("/nfs/freenas/tuph/e18/project/compass/analysis/cdittrich/Antok/build/bin/Completed_Runs/All_Data_PiKK.root", "READ");
  // Histogramme benennen und zuweisen
  TH3D* h3 = nullptr;
  f1->GetObject("MainTrainSoft/Dalitz KNegKPos versus KNegPi/Dalitz KNegKPos versus KNegPi_1111111111111_hist", h3);
  
  
  //Canvas erzeugen 
  auto c=new TCanvas("c","c",800,800);
  
  //Canvasfenster fuellen
  h3->Draw();
  
  h3->SetShowProjection("xy col");
}
